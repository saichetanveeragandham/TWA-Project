# TWA-Project

This project aims to assist individuals whose resumes are being rejected due to their criminal records by matching them with jobs where their crimes do not reflect negatively.


### Functional Requirements

1. Job Details:
   - Industry
   - Location
   - Accessibility
   - Contact Information
   - Positions Available
   - Salary
   - Benefits
   - Shifts Available
   - Offense Exemptions
   - Notes

2. Job Seekers:
   - Jobseeker First Name
   - Jobseeker Last Name
   - Jobseeker Phone Number
   - Jobseeker Email

### Business Requirements

The Transformative Workforce Academy aims to provide job opportunities to individuals with criminal records who are seeking to make a positive change in their lives. It creates opportunities for them by giving second chances and helping them find their dream jobs.

To achieve this, it is necessary to maintain records of job seekers and employer details.

### Initial Approach for the Project

![image](https://github.com/NavyaNelluri/Project-TWA/assets/123142678/bbf27237-df59-4606-81bd-5c7d836caf96)

The initial approach to this project involves the following steps:

1. Job seekers and employers will be asked to fill out Google Forms.
2. The information will be extracted in .CSV format and loaded into the database.
3. A framework will be created to access the database data, which includes:
   - Connection to the database
   - Loading data
   - Retrieving data
   - Mapping job seekers to appropriate job positions
4. The mapped data will be available on the front end, either by sorting based on employer details or job positions.

### Documentation of the CI/CD pipeline
This is a GitHub Actions workflow configuration file. GitHub Actions is a CI/CD (Continuous Integration/Continuous Deployment) tool provided by GitHub. It allows you to automate software workflows directly in your GitHub repository.

Here's a breakdown of the configuration file:

Event Triggers: The workflow is triggered on push and pull_request events to the main branch. This means that any time code is pushed to these branches or a pull request is made against these branches, the workflow will run.

Jobs: The workflow consists of a single job named test. Jobs are run on virtual machines. They can run at the same time in parallel or sequentially depending on their dependencies.

Runs-on: The test job runs on the latest version of Ubuntu. GitHub provides runners for Ubuntu, Windows, and macOS.

Steps: The test job has several steps. Each step in a job executes the same runner, allowing them to share data with each other. Steps can run commands, run setup tasks, or run an action in your repository, a public repository, or an action published in a Docker registry.

Checkout code: This step uses the actions/checkout@v2 action to check out your repository's code onto the runner.

Change directory: This step changes the current directory to "Directory given". This might be needed if the subsequent steps need to be run in that directory.

Install Node.js: This step uses the actions/setup-node@v2 action to install Node.js version 14.x on the runner.

Install dependencies: This step first changes the directory to #filelocation (you should replace this with the actual path) and then runs yarn install to install the dependencies for your project.

Run tests: This step also changes the directory to #filelocation (again, replace this with the actual path) and then runs yarn test to execute your project's tests.

This workflow is a basic example of a Node.js project's CI pipeline. It ensures that for every push or pull request, the project's dependencies are installed and tests are run. This helps catch and fix any errors quickly and ensures that the codebase maintains a good quality.

