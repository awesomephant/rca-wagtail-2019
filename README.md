# RCA Website Wagtail site

## Technical documentation

This project contains technical documentation written in Markdown in the `/docs` folder.

You can view it using `mkdocs` by running:

```bash
mkdocs serve
```

The documentation will be available at: http://localhost:8001/

## Contributing

1. Make changes on a new branch, including a broad category and the ticket number if relevant e.g. `feature/123-extra-squiggles`, `fix/newsletter-signup`.
2. Push your branch to the remote.
3. Make merge requests at e.g. https://git.torchbox.com/[client_name]/rca, no trailing slash/merge_requests/new, setting the 'Source branch' to your feature branch and the 'Target branch' to `master`. Select 'Compare branches and continue'.
4. Edit details as necessary.

Gitlab has built-in CI tests. These can be configured by editing `.gitlab-ci.yml`. By default these are run on all pushes and merge requests.

If you need to preview work on `staging`, this can be merged and deployed manually without making a merge request. You can still make the merge request as above, but add a note to say that this is on `staging`, and not yet ready to be merged to `master`.

### Code styleguide

This project’s code formatting is enforced with [Prettier](https://prettier.io/) for supported languages. Make sure to have Prettier integrated with your editor to auto-format when saving files, or to manually run it before committing (`npm run format`).

## Automatic linting locally

You can also run the linting tests automatically before committing. This is optional. It uses pre-commit, which is installed by default in the vagrant box, and a .pre-commit-config.yml file is included for the project.

To use when making commits on your host machine you must install pre-commit, either create a virtualenv to use with the project, or to install globally see instructions at (https://pre-commit.com/#install).

Pre-commit will not run by default. To set it up, run `pre-commit install` inside the Vagrant box, or on the host if you have installed pre-commit there.

# Setting up a local build

This repository includes a Vagrantfile for running the project in a Debian VM and
a fabfile for running common commands with Fabric.

To set up a new build:

```bash
git clone [URL TO GIT REMOTE]
cd rca
vagrant up
vagrant ssh
```

Then within the SSH session:

```bash
dj migrate
dj createcachetable
dj createsuperuser
djrun
```

This will make the site available on the host machine at: http://127.0.0.1:8000/

# Front-end assets

To build front-end assets you will additionally need to run the following commands:

```bash
npm install
npm run build:prod
```

After any change to the CSS or Javascript you will need to run the build command again, either in the vm or on your host machine. See the [Front-end tooling docs](docs/front-end-tooling.md) for further details.

## Deployment

The static assets should be automatically generated on deployment and you do
not need to commit them. The command used to generate the production version
of static files is `npm run build:prod`.

# Servers

VM should come preinstalled with Fabric, Heroku CLI and AWS CLI.

## Login to Heroku

Please log in to Heroku before executing any commands for servers hosted there
using the `heroku login -i` command. You have to do it both in the VM and your
host machine if you want to be able to use it in both places.

## Pulling data

To populate your local database with the content of staging/production:

```bash
fab pull-dev-data
fab pull-staging-data
fab pull-production-data
```

To fetch images and other media:

```bash
fab pull-dev-media
fab pull-staging-media
fab pull-production-media
```

To fetch only original images, with no extra media files and no renditions:

```bash
fab pull-dev-images
fab pull-staging-images
fab pull-production-images
```

## Deployments

To deploy the site to dev/staging/production:

```bash
fab deploy-dev
fab deploy-staging
fab deploy-production
```

## Connect to the shell

To open the shell of the servers.

```bash
fab dev-shell
fab staging-shell
fab production-shell
```

## Pushing database and media files

Please be aware executing those commands is a possibly destructive action. Make
sure to take backups.

If you want to push your local database to the servers.

```bash
fab push-dev-data
fab push-staging-data
fab push-production-data
```

Or if you want to push your local media files.

```bash
fab push-dev-media
fab push-staging-media
fab push-production-media
```

## Scheduled tasks

When you set up a server you should make sure the following scheduled tasks are set.

- `django-admin publish_scheduled_pages` - every 10 minutes or more often. This is necessary to make publishing scheduled pages work.
- `django-admin clearsessions` - once a day (not necessary, but useful).
- `django-admin update_index` - once a day (not necessary, but useful to make sure search index stays intact).
