# Project-TWA
Transformative workforce Academy - This project will help in giving second chance for the people who are having criminal records<br></br>
## Functional Requirements
1. Job Details:
  Job Details includes Industry, Location, Accessibility, Contact Information, Positions Available, Salary, Benefits, Shifts Available, Offense Exemptions, Notes.
2. Job Seekers:
  Jobseeker First Name, Jobseeker Last Name, Jobseeker Phone Number, Jobseeker Email.<br></br>
## Business Requirements
Transformative workforce Academy mainly aims in giving job opportunity to the people who are having criminal records and strongly wants to adapt a new change in their lives. It creates opportunity for them by giving second chances and helps them to find their dream job.

For this, we need to maintain records of job seekers and employer details.
<br></br>
## Initial approach for the project

![image](https://github.com/NavyaNelluri/Project-TWA/assets/123142678/bbf27237-df59-4606-81bd-5c7d836caf96)
Above is the initial approach to this project.
* On the first go, we will ask job seejers and employers to fill out the google forms.
* We will thenextract the information in .CSV format and then load it to database.
* On the next step, we create framework that access the database data.
  * Framework includes:
    * connection to the database
    * loading data.
    * retrieving data.
    * mapping job seekers to the appropriate job positions
* This mapped data will be available on the front end either by sorting based on employer details or with the job positions.
# Configuration
This file is used to configure GitHub Actions workflows. A CI/CD (Continuous Integration/Continuous Deployment) tool offered by GitHub is called GitHub Actions. It enables direct software process automation in your GitHub repository.

Here is how the configuration file is broken down:

Events that cause a push or pull request to the main or issue_6 branches set off the workflow. This indicates that the workflow will execute each time code is posted to these branches or a pull request is submitted against them.

Jobs: There is only one job in the process, which is called test. Virtual machines are used to run jobs. Depending on their dependencies, they can operate concurrently, in parallel, or sequentially.

Runs-on: The most recent Ubuntu version is used to execute the test job. GitHub offers runners for Windows, macOS, and Ubuntu.

The test job comprises a number of steps. The same runner is used to execute each phase of a job, enabling them to exchange data. Steps can execute commands, setup tasks, actions in your repository, actions available in a public repository, and actions made available in a Docker registry.

Check out code: In this phase, the code from your repository is checked out onto the runner using the actions/checkout@v2 action.

The current directory is changed to "remote" in this phase. If the next steps must be performed in that directory, then this might be required.

# Installation
Install Node.js: The actions/setup-node@v2 action is used in this stage to install Node.js 14.x on the runner.

Install dependencies: To install the dependencies for your project, first change the directory to #filelocation (you should replace this with the actual path). Next, execute yarn install.

Run tests: In this step, the directory is also changed to #filelocation (again, replace this with the correct path), and yarn test is then run to run the tests for your project.

This process serves as a simple illustration of a CI pipeline for a Node.js project. It guarantees that the project's dependencies are installed and tests are executed for each push or pull request. This keeps the codebase's quality high and makes it easier to find and remedy any issues.







  
