boys = {'Nilesh': 41, 'Soumitra': 42, 'Nadeem': 47}
girls = {'Rasika': 38, 'Rajashree': 43, 'Rasika': 45}
combined = {**boys, **girls}
print(combined)
combined = {**girls, **boys}
print(combined)
