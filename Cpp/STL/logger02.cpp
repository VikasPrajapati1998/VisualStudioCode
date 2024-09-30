// Here's an example of logging in C++ using the std::fstream class to write to a file:



#include <fstream>
#include <iostream>
#include <stdexcept>

using namespace std;

// Logging levels
enum LogLevel {
    DEBUG,
    INFO,
    WARNING,
    ERROR,
    CRITICAL
};

// Function to log messages
void logMessage(const std::string& message, LogLevel level) {
    std::ofstream logFile("log_file.log", std::ios_base::app);

    if (!logFile.is_open()) {
        throw std::runtime_error("Failed to open log file");
    }

    // Log level strings
    const std::string levelStrings[] = {
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL"
    };

    // Log message with timestamp
    logFile << "[" << __DATE__ << " " << __TIME__ << "] [" << levelStrings[level] << "] " << message << std::endl;
}

int main() {
    try {
        logMessage("This is a debug message", DEBUG);
        logMessage("This is an info message", INFO);
        logMessage("This is a warning message", WARNING);
        logMessage("This is an error message", ERROR);
        logMessage("This is a critical message", CRITICAL);
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}

/*


This code logs messages to a file named `log_file.log` in the current working directory, with each message prefixed with a timestamp and logging level.


For more advanced logging, consider using a dedicated logging library like:


*   `spdlog`
*   `log4cpp`
*   `glog`


These libraries provide additional features like:


*   Customizable logging levels and formats
*   Log rotation and file management
*   Multithreading support
*   Integration with system logs


You can install these libraries using package managers like `vcpkg` or `apt-get`.

*/