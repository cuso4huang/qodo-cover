cover-agent \
  --source-file-path="src/main/java/com/davidparry/cover/SimpleMathOperations.java" \
  --test-file-path="src/test/groovy/com/davidparry/cover/SimpleMathOperationsSpec.groovy" \
  --code-coverage-report-path="build/reports/jacoco/test/jacocoTestReport.csv" \
  --test-command="./gradlew clean test jacocoTestReport" \
  --test-command-dir=$(pwd) \
  --coverage-type="jacoco" \
  --desired-coverage=70 \
  --max-iterations=1 \
  --model="openai/deepseek-chat" \
  --api-base="https://api.deepseek.com"

  cover-agent \
  --source-file-path="src/main/java/com/example/calculator/controller/CalculatorController.java" \
  --test-file-path="src/test/java/com/example/calculator/controller/CalculatorControllerTest.java" \
  --code-coverage-report-path="target/site/jacoco/jacoco.xml" \
  --test-command="mvn clean test jacoco:report" \
  --test-command-dir=$(pwd) \
  --coverage-type="jacoco" \
  --desired-coverage=70 \
  --max-iterations=1 \
  --model="openai/deepseek-chat" \
  --api-base="https://api.deepseek.com"