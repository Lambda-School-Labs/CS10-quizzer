<div align="center">
<h1>Quizzer</h1>
</div>

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)
[ ![Codeship Status for Lambda-School-Labs/CS10-quizzer](https://app.codeship.com/projects/8ea07f40-9e5a-0136-7f9c-425a9ca03814/status?branch=master)](https://app.codeship.com/projects/306228) [![React](https://img.shields.io/badge/React-16.5-blue.svg)](https://reactjs.org/) [![Django](https://img.shields.io/badge/Django-2.1-green.svg)](https://www.djangoproject.com/) [![JavaScript Style Guide](https://img.shields.io/badge/code_style-standard-brightgreen.svg)](https://standardjs.com)

Quizzer is a simple web application for teachers to create quizzes and quickly distribute them to students via email. [Try it out.](https://quizzercs10.herokuapp.com/)

## Contents
1. [Our Project Stack](#stack)
    - [Why These Technologies?](#tech)
2. [Developer Documentation](#docs)
    - [Contributing](#contribute)
    - [Local Installation](#install)
    - [API](#api)
3. [Contributors](#contributors)
4. [License](#license)

## Our Project Stack <a name="stack"></a>
Quizzer is built on a straightforward stack: the client is a [React](https://github.com/facebook/react) application (created with [Create React App](https://github.com/facebook/create-react-app) and primarily built with [reactstrap](https://github.com/reactstrap/reactstrap) components), while the back-end is a [Django](https://www.djangoproject.com/) server, which both serves up the client itself, and delivers data to and from a [PostgreSQL](https://www.postgresql.org/) database (or, in a development environment, the default Django [SQLite](https://www.sqlite.org/index.html) database.)

Communication between the client and server is achieved through [GraphQL](https://graphql.org/), rather than traditional REST. To accomplish this, the client employs the [React Apollo Client](https://www.apollographql.com/docs/react/) client to properly format and parse requests and responses, while [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/) is employed server-side to receive, interpret, and respond appropriately to the client.

Lastly, our application is set up for continuous integration and automatic deploy: any updates to the `master` branch are first processed through [Codeship](https://codeship.com/) for testing and, assuming tests pass, deployed to [Heroku](https://heroku.com/) where it can be accessed by the end-user.

### Why These Technologies? <a name="tech"></a>

- **React:** This was a simple choice to make, both due to the team's familiarity with React, and because its component-based structure allows rapid implementation of a functional user interface with a minimum of effort.

- **Django:** Using Django allows us to access and save to a SQL-based database without needing to write cumbersone SQL queries, thanks to its simple MVC approach. Django also makes it trivial to serve the client directly, rather than needing to deploy client and server separately.

- **PostgreSQL / SQLite:** As our application makes use of relational data, e.g. which quiz is assigned to what class, it made sense early on to use a relational database, which are traditionally SQL based. Fortunately, Django integrates quickly with both SQLite, which it uses by default for development purposes, and PostgreSQL, which Heroku uses by default.

- **GraphQL:** The idea of sending and receiving ONLY data relevant to any function of the app, e.g. sending and receiving JUST the name of the classroom when updating the classroom's name, was appealing from the very beginning, as traditional REST will typically give you the entire box instead of the one item you actually want.

  - Accomplishing this communication was fairly simple to implement, as the Apollo Client integrates easily with React, providing components to quickly interpret and fire off GraphQL queries and mutations, while Graphene gives similar functionality to Django, integrating directly with schemas and models we had already created for the database.

- **Codeship:** In order to verify that any changes pushed to the `master` branch are viable for production, we integrated Codeship into our GitHub project to make use of automated build tests of both the server and the client. This also provides the same service to changes made to ANY branch, meaning that pull requests will clearly show a reviewer whether the changes have passed tests or not, prior to them directly reviewing those changes.

  - Additionally, we integrated Codeship into our Slack team channel, which displays messages when a build fails, or when a previously failing build is now passing. This allows us to stay apprised of any issues affecting any team member's work.

- **Heroku:** As we are using Django, we decided early on to simply allow it to serve up the client directly, rather than deploy our server to one service, and our client to another. This necessitated using a service which could support hosting a database in addition to serving up static assets, and Heroku fit that bill nicely.

## Developer Documentation <a name="docs"></a>

### Contributing <a name="contribute"></a>
WIP

### Local Installation <a name="install"></a>
WIP

## API <a name="api"></a>
WIP

## Contributors <a name="contributors"></a>
| [<img src="https://avatars3.githubusercontent.com/u/17170364?v=4" align="center" width=100><br><b>Brian Durbin</b> ](https://github.com/bdurb) | [<img src="https://avatars0.githubusercontent.com/u/29239201?v=4" align="center" width=100><br><b>Brandon Benefield</b>  ](https://github.com/bbenefield89) | [<img src="https://avatars1.githubusercontent.com/u/35475006?v=4" align="center" width=100><br><b>Edward Gonzalez</b>  ](https://github.com/eddygonzalez9708) | [<img src="https://avatars2.githubusercontent.com/u/26112479?v=4" align="center" width=100><br><b>Daniel Abbott</b>  ](https://github.com/Mephestys) |
|---|---|---|---|

## License <a name="license"></a>
Quizzer is [MIT licensed.](LICENSE)
