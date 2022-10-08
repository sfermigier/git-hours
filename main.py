#!/usr/bin/env python3
import os
import sys

import pydash as _
from devtools import debug
from git import Repo

# const Promise = require('bluebird');
# const _ = require('lodash');
# const fs = require('fs');
# const git = require('nodegit');
# const moment = require('moment');
# const program = require('commander');

DATE_FORMAT = 'YYYY-MM-DD'

CONFIG = {
  # Maximum time diff between 2 subsequent commits in minutes which are
  ## counted to be in the same coding "session"
  "maxCommitDiffInMinutes": 2 * 60,

  # How many minutes should be added for the first commit of coding session
  "firstCommitAdditionInMinutes": 2 * 60,

  # Include commits since time x
  "since": 'always',
  "until": 'always',

  # Include merge requests
  "mergeRequest": True,

  # Git repo
  "gitPath": '.',

  # Aliases of emails for grouping the same activity as one person
  "emailAliases": {
    'linus@torvalds.com': 'linus@linux.com',
  },
  "branch": None,
}


# # Estimates spent working hours based on commit dates
# def estimateHours(dates):
#   if dates.length < 2:
#     return 0
#
#   # Oldest commit first, newest last
#   sortedDates = dates.sort((a, b) => a - b)
#   allButLast = _.take(sortedDates, sortedDates.length - 1)
#
#   totalHours = _.reduce(allButLast, (hours, date, index) => {
#     const nextDate = sortedDates[index + 1];
#     const diffInMinutes = (nextDate - date) / 1000 / 60;
#
#     // Check if commits are counted to be in same coding session
#     if (diffInMinutes < config.maxCommitDiffInMinutes) {
#       return hours + diffInMinutes / 60;
#     }
#
#     # The date difference is too big to be inside single coding session
#     # The work of first commit of a session cannot be seen in git history,
#     # so we make a blunt estimate of it
#     return hours + config.firstCommitAdditionInMinutes / 60;
#   }, 0);
#
#   return Math.round(totalHours)
#
#
# def getBranchCommits(branchLatestCommit):
#   return new Promise((resolve, reject) => {
#     const history = branchLatestCommit.history();
#     const commits = [];
#
#     history.on('commit', (commit) => {
#       let author = null;
#       if (!_.isNull(commit.author())) {
#         author = {
#           name: commit.author().name(),
#           email: commit.author().email(),
#         };
#       }
#
#       const commitData = {
#         sha: commit.sha(),
#         date: commit.date(),
#         message: commit.message(),
#         author,
#       };
#
#       let isValidSince = true;
#       const sinceAlways = config.since === 'always' || !config.since;
#       if (sinceAlways || moment(commitData.date.toISOString()).isAfter(config.since)) {
#         isValidSince = true;
#       } else {
#         isValidSince = false;
#       }
#
#       let isValidUntil = true;
#       const untilAlways = config.until === 'always' || !config.until;
#       if (untilAlways || moment(commitData.date.toISOString()).isBefore(config.until)) {
#         isValidUntil = true;
#       } else {
#         isValidUntil = false;
#       }
#
#       if (isValidSince && isValidUntil) {
#         commits.push(commitData);
#       }
#     });
#     history.on('end', () => resolve(commits));
#     history.on('error', reject);
#
#     // Start emitting events.
#     history.start();
#   });
# }
#
#
# def getBranchLatestCommit(repo, branchName):
#   return repo.getBranch(branchName).then((reference) => repo.getBranchCommit(reference.name()));
#
#
# def getAllReferences(repo):
#   return repo.getReferenceNames(git.Reference.TYPE.ALL)


# Promisify nodegit's API of getting all commits in repository
def getCommits(gitPath, branch):
  repo = Repo(gitPath)
  commits = list(repo.iter_commits(branch))
  return commits

#   return git.Repository.open(gitPath)
#     .then((repo) => {
#       const allReferences = getAllReferences(repo);
#       let filterPromise;
#
#       if (branch) {
#         filterPromise = Promise.filter(allReferences, (reference) => (reference === `refs/heads/${branch}`));
#       } else {
#         filterPromise = Promise.filter(allReferences, (reference) => reference.match(/refs\/heads\/.*/));
#       }
#
#       return filterPromise.map((branchName) => getBranchLatestCommit(repo, branchName))
#         .map((branchLatestCommit) => getBranchCommits(branchLatestCommit))
#         .reduce((allCommits, branchCommits) => {
#           _.each(branchCommits, (commit) => {
#             allCommits.push(commit);
#           });
#
#           return allCommits;
#         }, [])
#         .then((commits) => {
#           // Multiple branches might share commits, so take unique
#           const uniqueCommits = _.uniq(commits, (item) => item.sha);
#
#           return uniqueCommits.filter((commit) => {
#             // Exclude all commits starting with "Merge ..."
#             if (!config.mergeRequest && commit.message.startsWith('Merge ')) {
#               return false;
#             }
#             return true;
#           });
#         });
#     });
# }


# def parseEmailAlias(value):
#   if (value.indexOf('=') > 0):
#     const email = value.substring(0, value.indexOf('=')).trim()
#     const alias = value.substring(value.indexOf('=') + 1).trim()
#     if (config.emailAliases === undefined):
#       config.emailAliases = {}
#
#     config.emailAliases[email] = alias
#   else:
#     console.error(`ERROR: Invalid alias: ${value}`)
#
#
# def mergeDefaultsWithArgs(config):
#   return {
#     "range": program.range,
#     "maxCommitDiffInMinutes": program.maxCommitDiff or config["maxCommitDiffInMinutes"],
#     "firstCommitAdditionInMinutes": program.firstCommitAdd or config["firstCommitAdditionInMinutes"],
#     "since": program.since or config["since"],
#     "until": program.until or config["until"],
#     "gitPath": program.path or config["gitPath"],
#     "mergeRequest": program.mergeRequest !== undefined ? (program.mergeRequest === 'true') : config.mergeRequest,
#     "branch": program.branch or config["branch"],
#   }
#
#
# def parseInputDate(inputDate):
#   match (inputDate):
#     case 'today':
#       return moment().startOf('day')
#     case 'yesterday':
#       return moment().startOf('day').subtract(1, 'day')
#     case 'thisweek':
#       return moment().startOf('week')
#     case 'lastweek':
#       return moment().startOf('week').subtract(1, 'week')
#     case 'always':
#       return 'always'
#     case _:
#       # // XXX: Moment tries to parse anything, results might be weird
#       return moment(inputDate, DATE_FORMAT)
#
#
# def parseSinceDate(since):
#   return parseInputDate(since)
#
#
# def parseUntilDate(until):
#   return parseInputDate(until)
#
#
# def parseArgs():
#   # function int(val) {
#   #   return parseInt(val, 10);
#   # }
#
#   program
#     .version(require('../package.json').version)
#     .usage('[options]')
#     .option(
#       '-d, --max-commit-diff [max-commit-diff]',
#       `maximum difference in minutes between commits counted to one session. Default: ${config.maxCommitDiffInMinutes}`,
#       int,
#     )
#     .option(
#       '-a, --first-commit-add [first-commit-add]',
#       `how many minutes first commit of session should add to total. Default: ${config.firstCommitAdditionInMinutes}`,
#       int,
#     )
#     .option(
#       '-s, --since [since-certain-date]',
#       `Analyze data since certain date. [always|yesterday|today|lastweek|thisweek|yyyy-mm-dd] Default: ${config.since}`,
#       String,
#     )
#     .option(
#       '-e, --email [emailOther=emailMain]',
#       'Group person by email address. Default: none',
#       String,
#     )
#     .option(
#       '-u, --until [until-certain-date]',
#       `Analyze data until certain date. [always|yesterday|today|lastweek|thisweek|yyyy-mm-dd] Default: ${config.until}`,
#       String,
#     )
#     .option(
#       '-m, --merge-request [false|true]',
#       `Include merge requests into calculation. Default: ${config.mergeRequest}`,
#       String,
#     )
#     .option(
#       '-p, --path [git-repo]',
#       `Git repository to analyze. Default: ${config.gitPath}`,
#       String,
#     )
#     .option(
#       '-b, --branch [branch-name]',
#       `Analyze only data on the specified branch. Default: ${config.branch}`,
#       String,
#     );
#
#   program.on('--help', () => {
#     console.log([
#       '  Examples:',
#       '   - Estimate hours of project',
#       '       $ git-hours',
#       '   - Estimate hours in repository where developers commit more seldom: they might have 4h(240min) pause between commits',
#       '       $ git-hours --max-commit-diff 240',
#       '   - Estimate hours in repository where developer works 5 hours before first commit in day',
#       '       $ git-hours --first-commit-add 300',
#       '   - Estimate hours work in repository since yesterday',
#       '       $ git-hours --since yesterday',
#       '   - Estimate hours work in repository since 2015-01-31',
#       '       $ git-hours --since 2015-01-31',
#       '   - Estimate hours work in repository on the "master" branch',
#       '       $ git-hours --branch master',
#       '  For more details, visit https://github.com/kimmobrunfeldt/git-hours',
#     ].join('\n\n'));
#   });
#
#   program.parse(process.argv);
# }


def exitIfShallow():
  if os.path.exists('.git/shallow'):
    print('Cannot analyze shallow copies!')
    print('Please run git fetch --unshallow before continuing!')
    sys.exit(1)


def main():
  exitIfShallow()

  config = CONFIG

  # parseArgs()
  #
  # config = mergeDefaultsWithArgs(CONFIG)
  # config.since = parseSinceDate(config.since)
  # config.until = parseUntilDate(config.until)

  # Poor man`s multiple args support
  # https://github.com/tj/commander.js/issues/531
  # for (let i = 0; i < process.argv.length; i += 1) {
  #   const k = process.argv[i];
  #   let n = i <= process.argv.length - 1 ? process.argv[i + 1] : undefined;
  #   if (k === '-e' || k === '--email') {
  #     parseEmailAlias(n);
  #   } else if (k.startsWith('--email=')) {
  #     n = k.substring(k.indexOf('=') + 1);
  #     parseEmailAlias(n);
  #   }
  # }

  commits = getCommits(config['gitPath'], config['branch'])

  debug(commits)

#   getCommits(config.gitPath, config.branch).then((commits) => {
#     commitsByEmail = _.groupBy(commits, (commit) => {
#       email = commit.author.email or 'unknown'
#       if (config.emailAliases !== undefined && config.emailAliases[email] !== undefined) {
#         email = config.emailAliases[email];
#       }
#       return email
#     });
#
#     authorWorks = _.map(commitsByEmail, (authorCommits, authorEmail) => ({
#       email: authorEmail,
#       name: authorCommits[0].author.name,
#       hours: estimateHours(_.map(authorCommits, 'date')),
#       commits: authorCommits.length,
#     }));
#
#     # XXX: This relies on the implementation detail that json is printed
#     # in the same order as the keys were added. This is anyway just for
#     # making the output easier to read, so it doesn't matter if it
#     # isn't sorted in some cases.
#     sortedWork = {}
#
#     _.each(_.sortBy(authorWorks, 'hours'), (authorWork) => {
#       sortedWork[authorWork.email] = _.omit(authorWork, 'email');
#     });
#
#     totalHours = _.reduce(sortedWork, (sum, authorWork) => sum + authorWork.hours, 0);
#
#     sortedWork["total"] = {
#       "hours": totalHours,
#       "commits": commits.length,
#     }
#
#     print(JSON.stringify(sortedWork, undefined, 2));
#   }).catch((e) => {
#     console.error(e.stack);
#   });
# }

main()
