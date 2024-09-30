#include <syslog.h>

int main() {
    // Open the system log
    openlog("logger", LOG_PID, LOG_USER);

    // Set the logging level
    setlogmask(LOG_UPTO(LOG_DEBUG));

    // Log messages
    syslog(LOG_DEBUG, "This is a debug message");
    syslog(LOG_INFO, "This is an info message");
    syslog(LOG_WARNING, "This is a warning message");
    syslog(LOG_ERR, "This is an error message");
    syslog(LOG_CRIT, "This is a critical message");

    // Close the system log
    closelog();

    return 0;
}

