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

widzę, że SSO w gitlabie działa, a w 2024 było CVE na SSO. Trzeba się przyjrzyć `CVE-2024-45409`.

oooo and SSO redirect as here 

![{45CA717B-6AF8-436F-B666-9C24C9EF49C8}](https://github.com/user-attachments/assets/ef951d3f-54a1-4376-b42f-a0532fb548f9)

![{0DB588D2-D73F-4180-A57D-EEC5CE1A7991}](https://github.com/user-attachments/assets/d23fc40b-3f22-4129-bac3-c468a2f5730d)

we can "decode" SAML Request using cyberchef

![{85369CC3-1A19-43BC-AE99-974C5D98ABAE}](https://github.com/user-attachments/assets/1dfa6809-44ec-4ce6-97a3-e622f74de301)

Now we need find valid username.

![{904ED26E-B1C0-4C07-B095-A94D96E1C9DE}](https://github.com/user-attachments/assets/98f50860-102c-486f-8c25-7bc555d630b8)

:(

by enumeration I found `satoru` and `akadmin`.

![{77E803CA-3115-4F50-A2BA-05541D950080}](https://github.com/user-attachments/assets/0a4d069c-6444-472b-9ff4-afb627283363)

![{894421EB-AE0D-4643-B405-42C721EBBD30}](https://github.com/user-attachments/assets/ec6a1410-0d39-470d-b9ea-1aff0800e738)


[https://gitlab.barrier.vl/satoru/gitconnect/-/blob/main/gitconnect.py](https://gitlab.barrier.vl/satoru/gitconnect/-/blob/main/gitconnect.py)
```
import requests
from urllib.parse import urljoin
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_gitlab_repos():
    base_url = 'https://gitlab.barrier.vl'
    api_url = urljoin(base_url, '/api/v4/')
    
    auth_data = {
        'grant_type': 'password',
        'username': 'satoru',
        'password': '***'
    }
    
    try:
        session = requests.Session()
        session.verify = False
        
        response = session.post(urljoin(base_url, '/oauth/token'), data=auth_data)
        response.raise_for_status()
        
        token = response.json()['access_token']
        headers = {'Authorization': f'Bearer {token}'}
        
        projects_response = session.get(urljoin(api_url, 'projects'), headers=headers)
        projects_response.raise_for_status()
        
        projects = projects_response.json()
        
        print("Available repositories:")
        for project in projects:
            print(f"\nName: {project['name']}")
            print(f"Description: {project.get('description', 'No description available')}")
            print(f"URL: {project['web_url']}")
            print(f"Last activity: {project['last_activity_at']}")
            print("-" * 50)
            
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {str(e)}")
        if hasattr(e.response, 'text'):
            print(f"Response text: {e.response.text}")
    finally:
        session.close()

if __name__ == "__main__":
    get_gitlab_repos()

```

![{64023B39-FF08-4BF4-8697-7140A2B6740D}](https://github.com/user-attachments/assets/7b225d25-3d5b-45a2-8267-69ecb041c3aa)

![{5184A25D-0289-4987-A489-14A834587232}](https://github.com/user-attachments/assets/80ea799b-c07c-4402-b68d-361c15f3c6cd)

![{2FC24FAE-E903-4C10-899E-67D4183B2A43}](https://github.com/user-attachments/assets/0643b1e2-1de0-4ef0-b3ce-cc2dbf69b430)

okey now we can use SAML exploit.

now SAML is huuge

![{63195DAE-8F75-41A8-9FDA-3CF3E8949793}](https://github.com/user-attachments/assets/650bcfd0-6821-46f5-b84e-e72c7bf742f0)

![{E6BBF712-00D1-41E8-984E-2F1E7C6862F4}](https://github.com/user-attachments/assets/64ca5614-5c64-40ca-a2aa-cd2339df1927)

![{6707BA66-02B4-4246-8DA1-CC3754695CBA}](https://github.com/user-attachments/assets/798243b6-b7ce-4b77-8c1f-bb7e020deff2)

And we are akadmin now

![{6BD10AD1-6FF2-47AD-ADB9-2A9DD1C97703}](https://github.com/user-attachments/assets/1382a321-080c-462b-8265-d9ccd94723b6)

I belive it's time to typical CI/CD exploitation.

In admin panel I found runner so.. it coundn't be hard to get RCE

![{38693341-419A-4E74-BE0B-7EAAD83AF763}](https://github.com/user-attachments/assets/bc101b78-da42-46a2-b5c0-9bdb74180638)




