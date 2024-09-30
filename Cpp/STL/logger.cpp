#include "spdlog/spdlog.h"
#include "spdlog/sinks/basic_file_sink.h"
#include "spdlog/sinks/stdout_sink.h"

int main() {
    // Create a logger
    auto logger = spdlog::get("logger");

    // Set the logging level
    logger->set_level(spdlog::level::debug);

    // Create a file sink to log messages to a file
    auto file_sink = std::make_shared<spdlog::sinks::basic_file_sink_mt>("log_file.log");

    // Create a console sink to log messages to the console
    auto console_sink = std::make_shared<spdlog::sinks::stdout_sink_mt>();

    // Set the logging level for each sink
    file_sink->set_level(spdlog::level::debug);
    console_sink->set_level(spdlog::level::info);

    // Set the formatter for each sink
    file_sink->set_formatter(spdlog::fmt::fmt("%+", "%Y-%m-%d %H:%M:%S.%e", "[", "] ", "{", "}", "", "", "", ""));
    console_sink->set_formatter(spdlog::fmt::fmt("%+", "%Y-%m-%d %H:%M:%S.%e", "[", "] ", "{", "}", "", "", "", ""));

    // Register the sinks with the logger
    logger->sinks().push_back(file_sink);
    logger->sinks().push_back(console_sink);

    // Now you can use the logger to log messages
    logger->debug("This is a debug message");
    logger->info("This is an info message");
    logger->warn("This is a warning message");
    logger->error("This is an error message");
    logger->critical("This is a critical message");

    return 0;
}
