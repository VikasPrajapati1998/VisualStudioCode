import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Model, Input
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.utils.class_weight import compute_class_weight
from keras.callbacks import ReduceLROnPlateau, EarlyStopping, LearningRateScheduler
from keras.regularizers import l2
from sklearn.metrics import accuracy_score

# Create the DANN model
class DANN(Model):
    def __init__(self, input_shape, num_classes):
        super(DANN, self).__init__()
        self.feature_extractor = keras.Sequential([
            layers.Dense(512, activation='tanh', kernel_regularizer=l2(0.003), input_shape=input_shape),
            layers.BatchNormalization(),
            layers.Dropout(0.4),
            layers.Dense(256, activation='sigmoid', kernel_regularizer=l2(0.003)),
            layers.BatchNormalization(),
            layers.Dropout(0.4),
            layers.Dense(128, activation='relu', kernel_regularizer=l2(0.003)),
            layers.BatchNormalization(),
            layers.Dropout(0.4)
        ])
        self.classifier = layers.Dense(num_classes, activation='softmax')
        self.domain_classifier = layers.Dense(2, activation='softmax')  # Two domains: source and target

    def call(self, inputs):
        features = self.feature_extractor(inputs)
        class_output = self.classifier(features)
        domain_output = self.domain_classifier(features)
        return class_output, domain_output

# Learning rate schedule
def lr_schedule(epoch, lr):
    decay_rate = 0.75
    decay_step = 3
    if epoch % decay_step == 0 and epoch:
        lr *= decay_rate
    return lr



# Load and preprocess data
train_df, test_df = EDA(train_cols, test_cols, 500)
drop_columns = [col for col in ["cement_quality", "Well_Name", "data_type"] if col in train_df.columns]
X = train_df.drop(columns=drop_columns)
y = train_df["cement_quality"]
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train-test split
X_train, X_val, y_train, y_val = train_test_split(X, y_encoded, test_size=0.1, random_state=42)

# Compute class weights
class_weights = compute_class_weight(class_weight='balanced', classes=np.unique(y_train), y=y_train)
class_weight_dict = dict(enumerate(class_weights))

# Create the DANN model
model = DANN((X_train.shape[1],), len(np.unique(y_encoded)))

# Create callbacks
early_stopping_reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=10, min_lr=0.0001)
early_stopping_val_accuracy = EarlyStopping(monitor='val_accuracy', patience=10, mode='max')
lr_scheduler = LearningRateScheduler(lr_schedule)

# Training parameters
batch_size = 32
epochs = 40

# Training loop
for epoch in range(epochs):
    print(f"Epoch {epoch + 1}/{epochs}")
    for (x_batch, y_batch) in zip(X_train, y_train):
        # Create labels for domains (0 for source domain)
        domain_labels = np.zeros((x_batch.shape[0],))
        
        with tf.GradientTape() as tape:
            # Forward pass
            class_output, domain_output = model(x_batch)
            
            # Calculate classification loss
            class_loss = keras.losses.sparse_categorical_crossentropy(y_batch, class_output)
            # Calculate domain loss
            domain_loss = keras.losses.sparse_categorical_crossentropy(domain_labels, domain_output)

            # Total loss
            total_loss = class_loss + domain_loss

        # Compute gradients and update weights
        gradients = tape.gradient(total_loss, model.trainable_variables)
        model.optimizer.apply_gradients(zip(gradients, model.trainable_variables))

        print(f"Loss: {total_loss.numpy():.4f}, Class Loss: {class_loss.numpy():.4f}, Domain Loss: {domain_loss.numpy():.4f}")

# Evaluate the model (validation)
y_pred, _ = model(X_val)
y_pred_class = np.argmax(y_pred, axis=1)
accuracy = accuracy_score(y_val, y_pred_class)
print(f"Validation Accuracy: {accuracy * 100:.3f}%\n")

# Prepare the testing dataset
drop_columns = [col for col in ["cement_quality", "Well_Name", "data_type"] if col in test_df.columns]
X_test = test_df.drop(columns=drop_columns)
y_test = test_df["cement_quality"]
y_test_encoded = le.transform(y_test)

# Test the model
y_test_pred, _ = model(X_test)
y_test_pred_class = np.argmax(y_test_pred, axis=1)
test_accuracy = accuracy_score(y_test_encoded, y_test_pred_class)
print(f"Testing Accuracy: {test_accuracy * 100:.3f}%\n")
