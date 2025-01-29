# Barrier
Linux, Medium, created by **xct**

```
22/tcp   open  ssh                 OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http                nginx
443/tcp  open  ssl/http            nginx
8080/tcp open  http                Apache Tomcat
9000/tcp open  cslistener?
9443/tcp open  ssl/tungsten-https?
```

robots.txt on 443 is huuuuuge
```
# See http://www.robotstxt.org/robotstxt.html for documentation on how to use the robots.txt file
#
# To ban all spiders from the entire site uncomment the next two lines:
# User-Agent: *
# Disallow: /

# Add a 1 second delay between successive requests to the same server, limits resources used by crawler
# Only some crawlers respect this setting, e.g. Googlebot does not
# Crawl-delay: 1

# Based on details in https://gitlab.com/gitlab-org/gitlab/blob/master/config/routes.rb,
# https://gitlab.com/gitlab-org/gitlab/blob/master/spec/routing, and using application

# Global routes
User-Agent: *
Disallow: /autocomplete/users
Disallow: /autocomplete/projects
Disallow: /search
Disallow: /admin
Disallow: /profile
Disallow: /dashboard
Disallow: /users
Disallow: /api/v*
Disallow: /help
Disallow: /s/
Disallow: /-/profile
Disallow: /-/user_settings/profile
Disallow: /-/ide/
Disallow: /-/experiment
# Restrict allowed routes to avoid very ugly search results
Allow: /users/sign_in
Allow: /users/sign_up
Allow: /users/*/snippets

# Generic resource routes like new, edit, raw
# This will block routes like:
# - /projects/new
# - /gitlab-org/gitlab-foss/issues/123/-/edit
User-Agent: *
Disallow: /*/new
Disallow: /*/edit
Disallow: /*/raw
Disallow: /*/realtime_changes

# Group details
User-Agent: *
Disallow: /groups/*/analytics
Disallow: /groups/*/contribution_analytics
Disallow: /groups/*/group_members
Disallow: /groups/*/-/saml/sso

# Project details
User-Agent: *
Disallow: /*/*.git$
Disallow: /*/archive/
Disallow: /*/repository/archive*
Disallow: /*/activity
Disallow: /*/blame
Disallow: /*/commits
Disallow: /*/commit
Disallow: /*/commit/*.patch
Disallow: /*/commit/*.diff
Disallow: /*/compare
Disallow: /*/network
Disallow: /*/graphs
Disallow: /*/merge_requests/*.patch
Disallow: /*/merge_requests/*.diff
Disallow: /*/merge_requests/*/diffs
Disallow: /*/deploy_keys
Disallow: /*/hooks
Disallow: /*/services
Disallow: /*/protected_branches
Disallow: /*/uploads/
Disallow: /*/project_members
Disallow: /*/settings
Disallow: /*/-/import
Disallow: /*/-/environments
Disallow: /*/-/jobs
Disallow: /*/-/requirements_management
Disallow: /*/-/pipelines
Disallow: /*/-/pipeline_schedules
Disallow: /*/-/dependencies
Disallow: /*/-/licenses
Disallow: /*/-/metrics
Disallow: /*/-/incidents
Disallow: /*/-/value_stream_analytics
Disallow: /*/-/analytics
Disallow: /*/insights
```

80 -> 443
443 -> is gitlab
8080 -> tomcat but... without completed instalation
9000 -> "authentik"
9443 ->  "authentik" but with ssl


![{6A9E5129-00E8-40F9-A64C-6634790AA490}](https://github.com/user-attachments/assets/005ef84d-53f9-4d95-9a51-d96af87ccb1f)

![{BD467C44-EEA2-42FA-86BD-58760116B4F1}](https://github.com/user-attachments/assets/659e8380-7d0e-4637-b03d-c9898ac6a850)

### Let's start testing

![{9DDD9C22-1910-4714-98D2-16CF36F0E8A0}](https://github.com/user-attachments/assets/fe136418-5c30-41df-959e-27a8c849fdde)

![{CA71783B-7E51-465A-ACAC-72EC2D6A8DC6}](https://github.com/user-attachments/assets/68d9dc48-3511-4aec-bb65-a0f362a5ed98)

`bartek:4jEZb9L1xMTvJ2rhDNIv`

![{6D5EEA81-352D-426D-85FF-764A3460B506}](https://github.com/user-attachments/assets/a08ebb5f-8ba2-4c7b-8cd6-4a3bbeeba8c4)

ok go next

lets run some content discovery
```
feroxbuster -u https://gitlab.barrier.vl/ -w ~/wordlist_discovery.txt -k
feroxbuster -u http://gitlab.barrier.vl:8080/ -w ~/wordlist_discovery.txt
feroxbuster -u http://gitlab.barrier.vl:9000/ -w ~/wordlist_discovery.txt (very slow like 10req/s)
```

at this moment we don't get only information about gitlab repos or users so let's explore other ports.

![{0A0CE3CC-5B23-4665-A4EF-EF77F646163E}](https://github.com/user-attachments/assets/d8fa6261-e608-4447-9a3c-f59f8489441e)

![{14CE5F85-24E7-4AD2-B07D-61F32947426B}](https://github.com/user-attachments/assets/88759fbe-28cc-4fa4-a8d4-45b00cd0950a)

401

![{8952F115-8B98-44A2-8FD3-315F97684BE3}](https://github.com/user-attachments/assets/0f0faf21-e84a-45a3-b6ba-eb4df498d49b)

when I tried the same credentions but on another endpoint browser automaticly send request to `http://10.10.109.89:9000/ws/client/`

maybe I should explore this `9000` port. 

![{8D8463A8-00FA-4C62-8517-DFB16948CAEE}](https://github.com/user-attachments/assets/201fdb9b-1737-4e04-ab7f-e97866eb330c)

looks nice.


