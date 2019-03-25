
add_library(elfspy
    Call.cpp
    ELFInfo.cpp
    Error.cpp
    Fail.cpp
    GOTEntry.cpp
    MFile.cpp
    Report.cpp
    SectionHeader.cpp
    SPY.cpp
)

target_include_directories(elfspy PUBLIC "${ELFSPY_INCLUDE_DIR}")
target_include_directories(elfspy PRIVATE "${ELFSPY_PRIVATE_INCLUDE_DIR}")
