import subprocess
import sys

# Read arguments from command line
test_arg = sys.argv[1] if len(sys.argv) > 1 else ""

if test_arg.__contains__("@"):
    # Construct the command to run the test with given tag
    command = ["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "reports", "--tags", test_arg]
elif test_arg.__contains__(".feature"):
    # Construct the command to run the feature file tests
    command = ["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "reports", test_arg]
else:
    # Construct the command to run all the tests
    command = ["behave",  "-f", "allure_behave.formatter:AllureFormatter", "-o", "reports"]

# Run the Behave tests with the specified options
subprocess.run(command)

# Remove skipped tests from the allure-results directory
subprocess.run("grep -rl '\"status\": \"skipped\"' reports | xargs rm -rf", shell=True)

# Generate Allure report
subprocess.run(["allure", "generate", "reports", "-o", "allure-report", "--clean"], check=True)
subprocess.run(["allure", "open", "allure-report"])
