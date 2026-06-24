MitieMicrosoft - regular technical check-in call-20260623_130026UTC-Meeting Recording
23 June 2026, 01:00pm
1h 15m 56s
Maha AbuRumman   0:15
Hello!
Poorna Bavapalli   0:17
Afternoon.
Maha AbuRumman   0:19
Good afternoon, how are we?
Vincent Rouet   0:21
Yeah.
OK.
Poorna Bavapalli   0:23
Just switched on the phone, hoping I will start live the next hour.
Maha AbuRumman   0:29
Let me know if you can hear any noise, because I've got the windows open, because there's a little bit of a breeze, but a lot of cars on the street, so...
Poorna Bavapalli   0:38
Nothing. We hear you okay. No background.
Vincent Rouet   0:41
Yeah, we okay.
Maha AbuRumman   0:43
Okay, good.
Poorna Bavapalli   0:45
Hi, Pankaj.
Pankaj Arora   0:48
Hello, hello, hi.
Vincent Rouet   0:50
Hello!
Poorna Bavapalli   0:55
Some of the schools are cancelling actually. Wish we had a holiday like an extra.
Maha AbuRumman   1:03
Yeah.
Poorna Bavapalli   1:06
Hi, Sourabh. Hi, Jordan.
Sourabh Sardesai   1:09
Hello!
Jordan Watkins   1:12
Hello, what's your name?
Poorna Bavapalli   1:13
Afternoon. Hi, Emma.
Vincent Rouet   1:15
Hello.
Poorna Bavapalli   1:27
How is the week going for Mitie?
Sourabh Sardesai   1:31
I'm good.
Mike Agar   1:31
Hi, guys.
Maha AbuRumman   1:33
Hello.
Poorna Bavapalli   1:33
Hi, Mike.
Mike Agar   1:38
So, do we have everyone we need?
Maha AbuRumman   1:41
Ohh.
Mike Agar   1:45
I think we do.
Maha AbuRumman   1:48
Oh.
Poorna Bavapalli   1:49
Look.
Mike Agar   1:50
Goutam can't make it today. We've got some of the data guys coming along later, maybe to talk about databases, but I think...
For Agent 365.
We've got everyone we need. So obviously we've got the members of the dev team, which I think you guys know, so Pankaj, Sourabh and Emma, I guess I'll include you in that as well, the sort of technical space. Colin is from our support teams, so obviously, you know, interested in keeping an eye on agents and how that's going to work in future.
Poorna Bavapalli   2:07
Yeah.
Mike Agar   2:20
Obviously, Jordan, I think you probably know from our InfoSec team.
And Alex is here from our data team. So again, probably more interested in the database conversation, but obviously involved in Prio, so will be interested in this as well. So just in terms of the agenda for this call, I think what we're aiming to do is go through Agent 365, get a bit of a demo, make sure we're all clear on what it does, where its boundary is in terms of its kind of capability and what it does and doesn't do, just to make sure we're all aware of that.
because I think maybe, maybe it's just me, but there's some degree of confusion on kind of where the boundary is with other tools. Obviously, that will then help us as we move forward with observability, which I think one, we're going to try and get something in next week on sort of wider observability. Is that right?
Poorna Bavapalli   2:51
Yeah.
Yeah, next week we'll see foundry control plane and any other questions probably after that, because there are a few areas of technology where we need to focus, but probably we will evolve over it next few weeks.
Mike Agar   3:06
Yeah, OK.
Yeah.
Okay, yeah.
Poorna Bavapalli   3:17
OK, on our end, we have Mohammed who will take us through the session, and we have Gemma as well. They both are on the security side.
Maha AbuRumman   3:27
Yeah, good afternoon, everyone. So, my name is Mohammed and I with me, Gemma. We're kind of a tag team, if you will, on the security side. So I tend to cover more the data security requirements capabilities. So if you've heard of Purview, that's usually my space. And then Gemma covers, unfortunately for her, everything else. So Defender, Sentinel, and
etc. And then with H35, we're kind of both on it because it spans pretty much all of it really. So I am going to share my screen. Please bear with me. My Team interface has changed, so I'm still learning as per usual. Can you see my screen now?
Poorna Bavapalli   4:06
Yeah.
Maha AbuRumman   4:08
Perfect. Okay. I'm not going to spend like a lot of times on slides or anything like that. I just wanted to walk through a couple, essentially, but we will spend most of our time within the demo platform and then come back to slides later for me to talk about roadmap and what's coming down the line.
So Mike, one thing to maybe mention is obviously Agent 365 went GA on the 1st of May. However, the development is very fast and very quick since it's gone live. A lot of previews have already also been added and preview features have already been activated, etc.
So there's a lot on the roadmap that will be landing in July and other capabilities will be landing for around a year. So just one thing to keep in mind is it's a fast moving space. And it's a fast moving space because AIAgentHelpdesk and AI is a fast moving space, as I'm sure we are all aware. And from an Agent 365 perspective,
It's not an agent, it's not AI. It is designed to be your platform to observe, govern, and secure agents essentially. So those are the three pillars that we are building the capabilities that we are offering around. And when we kind of started building this,
I think one thing Gemma and I constantly hear is there's too many portals for Microsoft products to go into. So very conscious of that and very conscious that a lot of our customers are already using capabilities that we already have. We didn't necessarily want to introduce yet another portal that you're managing things from.
And we didn't want to introduce new technology. They have to learn and kind of keep up, keep up with, etc. So Agent 365 is built on top of Purview Defender, etc. And it's providing that governance observability layer on top of all those solutions. And it can then integrate with
your Foundry, your profile studio, or potentially other agentic development platforms to bring in and sync to your registry so you can have that view of what agents are in the organization. But the premise is the same platform you're using to manage human identities, you're also then using to manage agentic identities, the same platform you're using.
using to secure your data, you would also use to secure agent data interactions and so on.
Any questions on this?
By the way, feel free to interrupt me. I do not like talking to myself.
Mike Agar   6:45
Okay.
I do have questions, Maha, but I think you're going to cover them as I go on, so I'll hold them back for now.
Maha AbuRumman   6:49
Yep.
Okay, cool.
All right, so access to Agent 365 is via the Admin Center. So you might hear it being referred to as MAP, which is the Microsoft Admin Center. And within the Microsoft Admin Center, you'll see the Agents section. There are role-based permissions associated with this.
Poorna Bavapalli   7:08
Yeah.
Maha AbuRumman   7:15
The AI administrator, which is highly privileged, and then...
the roles that were also introduced. I believe AI developer role is coming down the line if it's not there already. So there are role-based access controls associated or that have been built in to give you access or to give the different personas access to this. From within the agents overview page, I get a view of the number of agents that are potentially
active in the organization. And then I can also see a few different kind of metrics. I apologize, I am going to be flipping back and forth between a couple of environments just because I have my own environment that I'm trying to develop a build in. So I have admin controls and then I have a different environment that actually has proper dummy data.
So I'll flip back and forth between the two. But I can see in here, there's about 14,000 agents active or available, if you will, in the organization, number of active users. I can see some kind of insight. Yeah. No, please go ahead.
Sourabh Sardesai   8:12
APP.
Sorry, and they're all, and they're all from all the platforms from Microsoft, right? Foundry, yeah, yeah, cool.
Maha AbuRumman   8:18
Yeah, we're gonna we're gonna go into that.
Yeah, I'll show you what it is. Some of it is going to be whatever has been developed internally in your organization, potentially. Some of it will be whatever Microsoft provides or third party integrations.
Sourabh Sardesai   8:30
Thanks.
Maha AbuRumman   8:32
No worries. And then I can also see things that I need to potentially take action on. So pending requests for agents. So if development teams, if you're building something in Foundry and you want to get that published, we can route the request for publishing into Agent 365, and we'll take a look at that in a second. Agents at risk, so any type of risky detections that might be picked up by Defender or by Purview will also be routed into.
to hear any orphaned agents. I think one of the big concerns that a lot of my customers had with the kind of agenthelpdesk adoption is agents pro because people experiment, people build. Just to give you a kind of a sense, in January we had a customer event where...
Some of our internal Microsoft people were presenting and in January, on January 19th, my colleagues mentioned that within Microsoft, we had about 220,000 agents, which is almost as many as humans. And then a month after that, the number had already doubled because we had another event where they presented again and the number had already doubled.
And the reason is because people are experimenting, they're building, whether it's with Agent Builder, whether it's with Copilot Studio, whatever it is, and it creates this sprawl. And a lot of those agents that we probably have in our environment are potentially obsolete. People built them just to try something. I am guilty of that. Like I will go and try and build an agent.
and then never use it again, and so on. So you get a lot of that sprawl that is potentially expanding your risk landscape because those agents could be exposing you to risk. So if there are any orphaned agents, you get a view of that here. People might, you know, build something, lead the organization, it remains orphaned.
So you can then assign those to somebody else, any kind of exceptions or errors. And then you get some kind of statistics around which platforms have the most number of agents in them and trending agents by the number of active users and so on.
But if I go to my explore all agents page, I can see in here all of the agents that are available, again, available to use. That doesn't mean they're all being used, but are available to use. And I can philtre this across different platforms. So whatever's been built in Studio, Foundry, SharePoint, or even Amazon Bedrock,
or others. So I have a few here that have come in from my registry sync or connexion into Amazon Bedrock. So we can sync Agent 365 with other platforms. This is a preview capability literally been added in the past couple weeks. I want to say.
Right now, there's about four of them that we can build external connexions to, Amazon, Bedrock being one. But again, you also have the option of if you have a third party that is building agents for you, getting them to use Agent 365 toolkit so that you get that observability and you
get those agents synced into the platform.
Sourabh, does that answer your question?
Sourabh Sardesai   11:36
I want to ask one more on top of that. So the agents which are which are in Foundry, when do they start appearing here? Before publishing or by after creating the agents?
Maha AbuRumman   11:38
Yeah, please.
Yeah.
As soon as you create an agent, it is provisioned with an entra identity, and then it will appear here. So before it's published, even when it's still in dev, when you haven't done anything with it beyond give it a name.
Sourabh Sardesai   11:59
Now, okay, for example, we have dev, test, and...
Maha AbuRumman   11:59
It appears.
Sourabh Sardesai   12:04
environment with the same name for example, how does that how does that reflects here and how do we manage the duplication?
Shoots.
Maha AbuRumman   12:15
I will need to double cheque on that for you. I don't, unless Vincent, if you know off the top of your head, but you should be able to see like for Foundry agents, which environments they're coming in from and which channels or publishers they're coming in from, but you should be able to see the environment and the platform details in here.
Vincent Rouet   12:31
You will have the, yeah, the URL at the bottom here, which is your agent URI. That's where you would see your Foundry environments listed here, so it won't pick up automatically. So, say you have, you're talking about environments on Azure, right?
Sourabh Sardesai   12:40
Okay, so I'll have to...
I environments in Foundry, for example, I have, yeah, yeah.
Maha AbuRumman   12:48
Pankaj.
Vincent Rouet   12:48
Yeah, on Foundry. Yeah, so you will have the URL. That's how you would have to.
Sourabh Sardesai   12:52
And so...
Okay.
Vincent Rouet   12:54
Assess, yeah.
Sourabh Sardesai   12:56
Okay, so basically I'll see like based on how many environments we have, I'll see all of the agents there with the same name. Let's say there are four environments of 1 agent called Barry. So there will be 4 Barrys in the list. I have to click on them, open up and then cheque in the platform details which it belongs to.
Maha AbuRumman   13:06
Yeah.
Vincent Rouet   13:14
So, I would expect you probably, you know, after the from the portal, you can just click, click, click ups, you know, but in reality, you probably want to do that through a pipeline, so you might want to add some metadata somewhere in the publication in Agent 365 so that it's more obvious than having to click through each of them.
Sourabh Sardesai   13:37
For, for.
Vincent Rouet   13:37
That's probably.
Maha AbuRumman   13:37
Yup.
Sourabh Sardesai   13:39
For more higher level management audience, I'm not sure if they would be able to understand all that stuff, right?
Maha AbuRumman   13:42
Ha.
Yeah, so you can add more columns to that report, so you can bring in like the environment ID, if you will, or the deployment version channel, etcetera, and then the, like, you know, source and so on, if needed. Having said that, I do have a feedback, a feedback submitted to our products and engineering specifically to...
Poorna Bavapalli   13:45
Ohh, good.
Maha AbuRumman   14:06
add something in here to differentiate dev agents from prod agents. We have heard that from other customers, and I can add your name to the list to do that. Like I said, it is kind of quick changes happening on here, so hopefully when we have more customers requesting the same thing, that it does get prioritized.
Sourabh Sardesai   14:18
Right.
Maha AbuRumman   14:26
So, we can add that there.
Poorna Bavapalli   14:28
Currently, it can be achieved with that environment variable, isn't it, Maha? There was a variable where I think we can add, I think when they publish, we can set the variable. OK.
Maha AbuRumman   14:34
Yeah.
Yeah.
Pankaj Arora   14:37
So just adding on to what Sourabh's question was, I also wanted to know from a little higher level up, is for this tool, who's the actual target audience from Microsoft? Is it the engineers, the security ops guys, the finance, the senior stakeholders, the business, who's the target audience for this tool?
Poorna Bavapalli   14:37
Ha.
Maha AbuRumman   14:40
Mhm.
So.
It's hard to answer that question because I would say for different organizations, it's slightly different. The whole AI management thing is new. We usually see AICOE or an AI governance board or whatever, but this is more about administration management. So the same way you might have an endpoint
manager who might use Intune, then you'd have somebody who looks at agents and will be able to, and again, it depends on the rules and responsibilities and kind of the race scene in your organization. But through here, you get a view of what agents are available, you get a view if there are any active risks against them, you get a view of any requests submitted.
to publish agents in the organization. So I guess my question to you is who would be responsible for that within Mitie?
Pankaj Arora   15:47
So that's more sound like a security ops kind of audience in Mitie to me.
Maha AbuRumman   15:55
potentially. However, from a security perspective, we would expect security teams to kind of monitor, continue to monitor and continue to do things within the Defender Suite. Like I said, Agent 365 is built on top of Defender Purview and EnergyTeam. And so if we're looking at the SOC potentially responding to incidents that involve AI or involve agents,
They can do it directly from within Defender. Whoever will be responsible for managing work here will get a view of, oh, I have some risks reported against these agents. They will see under the security tab the risks were reported in Defender. But when they click on review, it takes them to the Defender tab.
They can see the related incidents and alerts. They can see what the incident was. So for example, this one, there was a gaolbreak attempt on an agent, right?
So from a SOC perspective, they continue to manage it with a vendor. But again, it depends on what the RACI is within Mitie. Like, is it going to be somebody in the security team that's going to approve agent publishing? Or is there going to be a centralised AI team, AI governance team, that manages the whole process of use case intake?
development, business value measurement, costing, finops, et cetera, that will potentially then be the role that will look at this.
Pankaj Arora   17:18
Yeah, so we do have AICOE as a governance board and within the board obviously we have people from all areas and domains and one of them being SecOps.
Maha AbuRumman   17:26
Mhm.
Pankaj Arora   17:27
So I assume it will be AICOE, but within AICOE, the SecOps plus the engineering team probably will have to work together with this tool.
Maha AbuRumman   17:37
Potentially, yes.
Pankaj Arora   17:38
sharing responsibilities and security and risk that this tool gives us. Okay, thank you. That answers my question. Thank you.
Maha AbuRumman   17:42
Yeah.
No, it's a good question. And I think just keep that question in mind as well as we continue to look through it, because there are a few different elements that maybe different people have to provide input into. Jordan, you got in hand up.
I.
Jordan Watkins   17:57
Yeah, and so from the risks that feed into the Defender portal, I'm assuming all that feeds into Sentinel as well, if they're all linked up.
Maha AbuRumman   18:01
Mhm.
Yeah, so if it's in Defender, it would feed into Sentinel.
Jordan Watkins   18:09
Yeah, yeah, okay.
Maha AbuRumman   18:12
It's the same incident queue that you would respond in today, essentially. So.
Jordan Watkins   18:16
Yeah.
Yeah, it makes sense.
Maha AbuRumman   18:19
Yeah, Sourabh, you've got your hand up. Yeah, sorry.
Jordan Watkins   18:20
And can, in the Defender portal, sorry, can you split them out by what was done by like an agent as a filter?
Sourabh Sardesai   18:22
Yeah.
Maha AbuRumman   18:33
I think, Gemma, do you know the answer off the top of your head? I think the impacted assets might be able to give you some of that.
Gemma Allen   18:41
That would probably be where I'd start looking. Let me just have a little note in that environment while you carry on. I'll come back in the. I'll come back.
Maha AbuRumman   18:43
Yeah.
Agar.
Yep.
Sourabh, you got your hand up as well.
Sourabh Sardesai   18:53
Yeah, so now that we know that this audience is mostly kind of technical, let's say if you have to build observability for business audience, is there a way to get the using APIs?
Maha AbuRumman   19:01
Mhm.
There are APIs early days still. Let me double cheque what you can pull from. Sorry, go ahead, Gemma.
Gemma Allen   19:16
Okay, I can make this a bit easier for you. So, the agentic assets that Maha is showing in the Agent 365 view here are also mirrored in the Defender portal. So there is also an agent's info table that's mirrored in the Defender portal. So you could use the APIs for that.
Maha AbuRumman   19:27
Yeah.
Gemma Allen   19:36
to go and get that information.
Maha AbuRumman   19:39
Yeah.
Sourabh Sardesai   19:39
And it will be automatically synced whenever any, yeah.
Gemma Allen   19:42
Yeah, yeah, the defended view is the...
Maha AbuRumman   19:42
Yeah.
Gemma Allen   19:45
Let's imagine it's a security person who has no access to the admin centre. That's for them to work in their security context to get a good overall understanding of the positioning of that agent in the business. They're not going to be doing the governance rules, but they are going to be involving incidents involving that agent.
Sourabh Sardesai   20:04
OK, is is there a business view for this this this data? Like, is there a...
Gemma Allen   20:04
Bye.
Maha AbuRumman   20:10
No, not currently, no.
Sourabh Sardesai   20:12
Cool.
Mike Agar   20:13
When you say not currently, does that imply a future plan that is coming soon to have one?
Maha AbuRumman   20:16
And.
What?
It kind of depends on what you want in a business view because I know there's conversations around like FinOps views for like agent consumption, et cetera, things like that. There is also like the Viva Insights dashboard, which I unfortunately don't have access to, but the Viva Insight dashboards gives you kind of some.
productivity metrics and things like that. So what is your definition of the business view?
Mike Agar   20:46
I guess we're thinking if, so we're on the more deep side of agents, right? So not so much like a co-pilot agent builder. So not really insights, but we're talking about if we've built 20, you know, complex agents that are running business processes within HR, we want to be able to give a HR admin some kind of dashboard that says,
Maha AbuRumman   20:53
Yeah.
Mhm.
Mhm.
Mike Agar   21:07
Of your 20 agents, this one costing you the most money. This one's running 20 times a day and this one's only running once. You know, this one's got a problem and it got stuck. So it's that business operational dashboard of their own agents.
Maha AbuRumman   21:12
Mhm.
Yeah.
Yeah, so I think once we start looking at the FinOps views and kind of bringing in the FinOps telemetry and analytics, you'll start to get some of that. I don't have a kind of timeline on that.
Mike Agar   21:31
But is the intention for that to go in here and Agent 365 to become a more business focused dashboard?
Maha AbuRumman   21:31
But...
I don't know, to be honest. No, I don't, I don't know. I, yeah, I'd like, they don't trust me enough to tell me that, but yeah.
Mike Agar   21:40
It's okay if you don't know the answer, by the way. I know I'm asking roadmappy questions.
Okay.
Maha AbuRumman   21:51
Okay, so like I said, registry, essentially you get a view of all potential agents that are available for the organization. So again, some of them could be built by you, some of them could be third party. So these are some of the third party ones that we've kind of built the integrations with or set up with when we went GA. So you can see a lot.
lot of the biggest ones out there. Again, I was having a conversation with a customer last week where they were like, well, we're having a third party build agents for us, or build something for us. How can we manage that? And this is where you can look at the SDK to onboard those agents. And then, like I said, the registry syncs.
Create scanners to other agenthelpdesk development platforms, so that you can start to bring in data by the agents published there.
Now, from another view, kind of view, if you will, if you look at the agent map, this starts to show you kind of a graphical representation of the agents in your organisation and again, which platforms they come in from. We're building capability into here to show you things like, for example, if I look at my
sales agent. I can see the connexions that it might have, how many users are using it, number of sessions. Similarly, with like co-work or researcher, etc. So if I click on, before I click on the agent, I can also see researchers connected to agents that operate in PowerPoint.
Excel and Word. And if I click on the old connections, it will show me kind of the connexions that it has to other agents.
This is again preview capability. We're building more and more into this. But the intent with this map is to show you connexions to other agents, but also connexions to potential tools that those agents might be using. So is it using like a work on queue MCP or another MCP, etc. So I can see that in the map view.
I can also see in here.
If I click on the details again, it opens up the flyout pane for me.
Depending on what the agent is, you might see more or less tabs if you will, but.
The flyout tab shows me details of what is this agent, so the description that you might have put in when you built it, any instructions that might have been provided, identity environment, users that it's installed for or available to. Difference between the two, you can have it automatically installed for HR team.
but also available for finance to download and install if they want to. Data and tools that it might be connected to, any security policies that it is scoped into, any permissions that it might have, recent activity, and then if it's allowed to initiate computer use,
And again, any agents that it is connected to and might be, you know, interacting with to perform any jobs that a user might give it. So I can see researcher here is connected to about 10 different agents.
So again, kind of some of the capability in these connections, if you will, et cetera, is in preview. You'll still be able to see the map today, but some of the capabilities are still in preview and they're kind of being added as we speak. So that is
Mike Agar   25:11
But this is this is great, right? This is the dashboard level.
Maha AbuRumman   25:13
Yeah.
That observability, yeah.
Mike Agar   25:17
kind of exact level, here's our mesh of agents and you click on one and it shows you which one that's talking to and this is your agentic mesh in a picture, right?
Maha AbuRumman   25:27
Essentially, that's what we're trying, like, that's what we're trying to get to, right? So right now...
For example, I don't see all the AMCPs, but the intent is to bring that in. But that is the intent to show you graphically, if you will, the connexions between all your agents. Pankaj, you've got your hand up.
Pankaj Arora   25:45
Yeah, so my question was, this is really a standard agent that's built by Microsoft 365 using the tools, right? This is not going to give us a similar view from Foundry, for example. If I have five agents, they talk to each other, is that going to automatically generate that kind of a view?
Maha AbuRumman   25:54
Yeah.
The intent long term is to do that, yes.
Poorna Bavapalli   26:03
Yes.
Pankaj Arora   26:05
OK, when we say long-term, anytime horizon, we talking three months, six months, and then...
Mike Agar   26:08
Ms.
Maha AbuRumman   26:10
I cannot commit to time horizons on behalf of my fellow engineers. However, I will tell you, those connections, that connexions view, or like that dotted line between the agents, did not exist 2 weeks ago. So this is how things are, how quickly things are moving.
Mike Agar   26:11
Ha.
Poorna Bavapalli   26:12
Team.
Pankaj Arora   26:27
Things are moving, yeah. Thank you.
Maha AbuRumman   26:29
Yeah, no problem. Sourabh, you got your hand up as well.
Sourabh Sardesai   26:32
Yeah, so, so for example, now if we if we create a workflow using MFM and there are a couple of multiple agents within that workflow, can we register the whole workflow as an entity in this?
Maha AbuRumman   26:49
Not at the moment. I don't know where we are in terms of like full, if you will, trace across agenthelpdesk interactions, but that's not something that we have right now.
Sourabh Sardesai   27:02
Okay, cool. Thanks.
Maha AbuRumman   27:02
And also, like...
I mean, for example, today, part of my role at Microsoft, like I could start speaking to Copilot for M365, and then Copilot might trigger the sales agent for me to let me know where I am kind of in terms of my opportunity or whatever it is. And then I might ask the sales agent a question and it might go, actually, I need to go and trigger this.
third agent because I'm asking for telemetry about, I don't know, customer usage or who is the contact. So I might need to trigger a marketing agent or something else. But that is the flow today. Tomorrow the flow might be different. So like I think.
Low traceability might be an interaction, but interaction thing, whereas connexions is more fixed. Does that make sense?
Sourabh Sardesai   27:54
Yeah.
Maha AbuRumman   27:55
Um...
Any other questions on the map?
Poorna Bavapalli   28:02
Do you want to see anything on the foundry bit? There was something on the foundry single to go pilots today.
Maha AbuRumman   28:14
Okay.
Poorna Bavapalli   28:15
No.
Maha AbuRumman   28:15
Sorry. So last one I wanted to touch on here is like the requests. So again, if you want to or when you...
build agents in Microsoft Foundry or in Copilot Studio today, and you publish them, you can have the request routed through Agent 365 or a central function to review the agent before it is widely published in the organization. You can still choose to allow people to
to share the agent. For example, in Microsoft, we all get dev environments within Copilot Studio to experiment and play around in. So again, I was trying to build an agent and I shared it with Gemma and a couple of other people on the team because I was trying to get them to test it for me.
but I cannot widely publish it across the whole organization. That's the activated.
So you can apply controls kind of environment level and then have the wide publishing requests route through Agent 365. So the request comes in through here. I can see details of what this agent is, the data and tools that it might be connected to. So this one, for example, will be connected to the work IQ mail MMC.
I also see what security policies it falls under. Defender are not yet showing up in here. The Defender capabilities will be going GA in July, different dates in July, but they should eventually be published in here as well. And I can also see permissions that this agent may or may not have to other tools and systems in the organization. So for example, this has API connexions
and Power Platform connector as well to execute activity. So before I allow or publish this agent, I can review all these details and make a determination. And kind of Pankaj back to your question earlier of who would be responsible for doing this. You can see it's kind of a mix of different functions.
I imagine when a user wants to build or develop an AI agent, you're going through some kind of risk assessment, security assessment, as well as business case, use case, et cetera. And as part of that, you're probably collecting information around what kind of data will it have access to, which systems will it have access to,
Are they create, read, update, delete permissions that it will have access to? So you can always compare kind of what is listed here against what the initial use case or business case for that agent was, and they make a determination of do we want to publish this or not?
Pankaj Arora   30:56
Yeah, okay, makes sense.
Maha AbuRumman   30:59
Brilliant. Another preview capability we have here is Shadow AI. So...
Poorna Bavapalli   31:04
Yeah.
Maha AbuRumman   31:06
OpenClaw being the starting point. But basically, this is looking at, are there any active agents on managed devices? So are people using OpenClaw to build agents on their device and using those agents on their devices? We started with OpenClaw. We'll be adding more to this list.
Under the ToolsOrToys section, you'll be able to see a registry of the MCPs that are available in the organisation that people could potentially be using as part of the dev.
And then again, any requests for adding more MCPs. Under the settings section is where you can set up some policy templates, if you will. So policy templates here, there are a couple out-of-the-box where you have default policy template for agents.
And this one specifies that any agent that gets published will have identity protection, network visibility, purview audit enabled, data security controls, AI compliance assessment. So there's like a baseline of policies that any activated agent or published agent will be included into or monitored by.
So the same way you're creating like a compliance profile or a configuration profile in Intune to manage devices, you'll have kind of something similar where you have a template to apply to agents, Jordan.
Jordan Watkins   32:29
And these templates are customizable so we can deploy our own.
Maha AbuRumman   32:34
Yes, again, given the capabilities in Defender are not yet live, you wouldn't see them in here. I'm going to just go into my environment where I can actually create stuff. I can go in here, agents without an identity, agents with their own identity, and then I can choose, for example, for
For conditional access, these are the policies I want to use. These are the access packages I want to use. Security baseline, sorry, security attributes that we might tag for this agent. So I might say it will be for engineering. And then there's a set of default policies that would be applied either way.
Jordan Watkins   33:15
Okay, my next question. So we have purview throughout Mitie and we label all of our documents. So is there a way to create, say, a policy that would say any agent being built can't access highly confidential or confidential? So then when it's pulling those documents, if it notices any of those, it doesn't reply that data back to the end user?
Maha AbuRumman   33:20
Mhm.
No, that's not possible right now. Is there a reason? Can you just kind of walk me through what the purpose of that would be or why?
Jordan Watkins   33:52
Just so if I was, we wouldn't necessarily want to upload any, you know, highly confidential documents to an agent. So if I, you know, give an agent a mighty highly confidential document and say, summarise this, I wouldn't necessarily want people to be able to do that with a document.
Poorna Bavapalli   34:10
Yeah.
Jordan Watkins   34:12
of that classification.
If it's just a standard internal document, it doesn't matter.
Maha AbuRumman   34:18
Yeah.
Jordan Watkins   34:19
But if it's something that's highly confidential, you probably don't want an agent viewing it and, you know, that data being stored somewhere on a Microsoft database or whatever that it is.
Maha AbuRumman   34:31
Right, so, and this is kind of why I'm asking.
We have a DLP capability.
I don't know if you looked at the DLP for co-pilot.
Jordan Watkins   34:46
It's not something I've seen.
Maha AbuRumman   34:46
So we have.
Okay, so we have a DLP capability where I could basically set up a DLP policy that says.
Poorna Bavapalli   34:52
Yes.
Maha AbuRumman   34:55
If a user tries to access a file with label Copilot exclusive, is what I called it in my demo environment, then Copilot cannot process that file.
The user can still access the file, the user can read the file, but Copilot will not function on the file.
Jordan Watkins   35:16
Okay, that makes sense. I think that's what I'm sort of looking for, to be honest.
Maha AbuRumman   35:20
Okay, I don't, I wouldn't say that's something you can extend today to all types of agents. But again, long term would be looking at expanding scope.
Jordan Watkins   35:27
Mhm.
Poorna Bavapalli   35:33
And probably every agent that build, what is the source data they are giving, right, Jordan? Probably that's where the philtres have to come in as well as centered. Like if someone is building an agent in Foundry, is the source data, if the source data shouldn't be using the high confidential one, then they shouldn't have an access to that as one.
Maha AbuRumman   35:45
Mm.
Poorna Bavapalli   35:53
that level, yeah, go for it.
Ha Duong   35:56
I did have a conversation similar with PG that day. I think for agent, the M265 agent, DRP policy is kick in. So whatever DRP that you have, that can kick in. Similar with Copalo Studio. The gap is in the.
The Foundry, but yeah, and then and then this is the same thing, like they they has to the agent when you build the agent, it need to be granted access to something by AI search or to a storage account or to a SharePoint.
Maha AbuRumman   36:14
Country.
and third-party agents.
Ha Duong   36:34
If the user doesn't have the access to it and if the agent do not have the access to it by RBAC and so on, they wouldn't be accessed to build that agent anyway.
If someone that say...
Cheque the document.
intentionally and then move it somehow and copy the content and separate it into a separate thing and inject that text into Agent, then yes, that's something that's different.
Poorna Bavapalli   36:53
The.
Maha AbuRumman   37:04
Yep.
And again, there would be things we can do today to limit that. So we, I don't think Mitie has this, but we have network DLP capabilities through integration with Entra Global Secure Access or.
my boss and I forgot who the other one, I think it was NetScope, SASE solutions essentially, but we could potentially use network DLP capabilities to also monitor what users are uploading into agents or applications and so on and again block that happening or stop that happening.
Jordan Watkins   37:40
Yeah, okay, that makes sense. I think a good call from that was that you'll have integrations with our boss, and that's who we use for our web proxy, so...
Maha AbuRumman   37:50
Yep.
So, we could do if that's your if I boss if you have the I boss SASE capabilities then with DLP you can integrate with that today to do network DLP.
Jordan Watkins   38:00
OK.
OK, sounds good. Maybe I'll pick that up with our account manager, see what we have, see if it's possible.
Maha AbuRumman   38:08
Yep.
So like I said, from within Agent 365, you'll be able to get a view of any agents that are at risk that could potentially kick off workflows to speak to the SOC and say, can you review these alerts, address these alerts? You get a visual representation of what is happening there.
You also have within purview a view of agent risks. So within Insider Risk Management, we now have policies that can be targeted at agents specifically. So in this example, I can see an agent that I have has potentially
perform some risky activity. So there was sensitive responses being generated and sensitive.
or risky prompts being entered into this agent.
And I can view these events and kind of what user performed the activity, what AI application it was done against. So this was against one of the Foundry agents. Any kind of sensitive data that might have been pulled out. I can see the response that the agent provided as well.
So for investigation purposes, we're no longer just looking at people as potential insider threats, but agents themselves can also be viewed as an insider threat. Do you use insider risk management today?
Jordan Watkins   39:40
Yes, I believe so. I believe it's configured within our purview.
Maha AbuRumman   39:45
OK.
So you can start to look at the agent risk policies. And I think there's a default one that you might have already in your environment out-of-the-box. You can start to look at the agent policies as well and kind of monitor agent interactions.
Worth mentioning is within Purview under DSPM, you'll see the AI observability dashboard. With Agent 365, this gets lit up. Again, it will kind of mirror a view of the agent registry numbers. You'll see the various agents. You'll also be able to see things like, hey, this is potentially
showing an oversharing risk, sensitive activity or sensitive information being put into it. So you can see risk levels, if you will, and the potential risk each of these agents presents. I can dive into the agent page itself. Again, I see the name of it.
I see the risk level and why, because there are two active risk alerts, for example, in here, the risk activities that I can view. And then we also provide some recommendations. So it might be like, okay, you might want to investigate the potential insider risks, or you might want to identify which sensitive information was used and protect that maybe with DLP policies, et cetera.
So the platform is kind of trying to give you recommendations in terms of how do we address any risks that these agents present. And from here, you can go to review the alerts, auto label the knowledge sources, create retention policies, and so on.
   41:04
I.
Maha AbuRumman   41:17
Jordan, you got your hand up.
Jordan Watkins   41:19
Yeah, sorry, keeping on. And is this part of our E5 licence or is this part of the new E7?
Maha AbuRumman   41:20
No, please.
No.
This would be part of Agent 365. So either E7 or Agent 365 separately.
Jordan Watkins   41:33
Okay.
Mike Agar   41:34
So we wanted to roll this out.
Maha AbuRumman   41:35
Ha.
Mike Agar   41:37
sorry, to a bunch of business managers and technical support team people. All of those people today, I think, would have three E5 licenses. This would be an additional cost.
Maha AbuRumman   41:39
Yeah.
Yes, yes.
Agent 365 is an additional SKU or is a separate SKU. So it would like, and I just wanted to clarify, it's the AI observability specifically that's part of Agent 365. The rest of DSPM you'll have available as part of E5.
Happy to walk you through what DSPM is for, but the AI observability specifically is part of Agent 365.
Mike Agar   42:10
Ha.
OK.
Maha AbuRumman   42:18
Um, yeah, it's a separate scheme, Vincent.
Vincent Rouet   42:22
Do you know if there's some additional licences requirements if they enable purview in Foundry and say they have 10 Foundry instances or let's say 6, how would that work?
Poorna Bavapalli   42:34
Yeah.
Maha AbuRumman   42:35
Um...
If you have agent 365.
Poorna Bavapalli   42:39
Play.
Maha AbuRumman   42:40
Monitoring for any agents built in Foundry is built into the Agent 365 licensing.
Vincent Rouet   42:48
OK.
Maha AbuRumman   42:49
So, okay, sorry, let me take a step back. Do you know or are you aware of how Agent 365 is licensed?
Poorna Bavapalli   42:57
Yeah.
Vincent Rouet   42:58
No, I just know there's toggle buttons on Foundry and just know what are the consequences of doing that. Sorry, I'm on the other side.
Maha AbuRumman   43:04
I meant, I meant the mighty team as well, OK.
Mike Agar   43:06
No.
Maha AbuRumman   43:08
Okay, so the way Agent 365 is licenced is per user. So this is the same way you licence for E5, you know, everybody in the business or whatever, Agent 365 licences is the same. We're not licencing agents, we're licencing people. So Vincent might have access to 10 agents and I might have access to 10.
Vincent Rouet   43:13
Thanks.
Yeah.
Maha AbuRumman   43:27
1000 agents. It doesn't matter. I might have built 5 agents, an agent might have, and Vincent might have built 100. It doesn't matter. I need to have a licence for you to benefit from the telemetry in Agent 365. There's various reasons why we did it this way. Most importantly, predictability for customers, right?
But if you get Agent 365 licenced for your users, then any agents that those users are using, building, sponsoring, owning, et cetera, will then also be, and you'll be able to monitor them with Purview, Defender, they'll get Entra identities and all of that good stuff. So you wouldn't have to pay separately for that.
However, if you're building AI capability within Azure for Foundry or Azure AI, that's not AIAgentHelpdesk, that has a consumption cost. So if you're training your own models, if you're building AI applications, like that then has a separate cost to Agent 365. But from an AIAgentHelpdesk perspective,
Poorna Bavapalli   44:13
Yeah.
Maha AbuRumman   44:29
Agent 365 should cover you for Preview Defender Intra capabilities.
Does that make sense, Vincent? Does that answer the question?
Vincent Rouet   44:39
Yeah, I think that would be good to have that in the transcript for the benefits of next steps with the Foundry next week. Yeah, thank you.
Maha AbuRumman   44:48
A couple other.
Other things I wanted to touch on quickly, like I said, any agents you create automatically get provisioned with an intra-agent identity.
Poorna Bavapalli   44:52
IT.
Maha AbuRumman   45:00
So within Entra, you'll now see an agent section. I can go into here and I can see all the agent identities. This tool will create identities for boundary agents, Copilot Studio agents. Agent builder agents do not yet get an identity.
Any agent you integrate via SDK will get an identity here as well. But like low code, so sorry, no code agents like SharePoint agents, agent builder agents do not yet get an identity.
Poorna Bavapalli   45:28
The.
Maha AbuRumman   45:32
For each of these agents, like I said, they get an ID. You also get agent blueprints. When we start thinking about potentially digital workers or autonomous agents, if we're starting to, I don't know, build agents that you might create multiple instances of or copies of. So Mike, you have one that is your assistant and I have one that's my assistant.
it might be multiple agents, each with a distinct identity. So we can differentiate. This was Mike's Barry that did it versus Maha's Barry that did it. I don't know why Barry is the only thing that came to mind right now, but we're going with it. So like being able to differentiate, again, going back to that traceability and objectability, each agent.
It will be a copy of the blueprint. The blueprint will dictate what conditional access policies, what access packages, entitlements it has, but each agent has its different identity, essentially. And then when we start thinking about digital workers, you might then have digital workers who might have their own mailbox.
or a OneDrive or whatever else, like collaboration and productivity tools that they will need, then we create an agent user account, not just an identity. Does that make sense?
That might be a little bit too much detail for the majority of the audience here, but yeah, Jordan, go ahead.
Jordan Watkins   46:48
Yeah.
And I'm assuming that's where you would apply the conditional access policies to the identities.
Maha AbuRumman   46:59
The identities, yes.
Jordan Watkins   47:00
Yeah.
Maha AbuRumman   47:03
Finally, there is a new portal. If you have a function or a role that is like an AI governance lead or an AI security risk lead, etc, this might be a portal they come into. I will caveat and say this portal is kind of still in the works.
There's very little in here for now, but it is the security dashboard for AI. And it's going to give you that inventory view, any potential misconfigurations or attack paths, agents that have sensitive interactions. And it will also provide recommendations in terms of what policies you might want to turn on.
Again, I'll see the inventory view in here. I'll get a view of agents, AI models that might be in use or available, and whether or not they are covered by
Poorna Bavapalli   47:49
You.
Maha AbuRumman   47:52
Defender or our security solutions, MCP servers, and other AI apps.
The reason there is a new portal, like I said, with kind of AI, we're seeing AI COEs, AI councils, AI boards, or an AI governance lead role kind of becoming a big part of this. And a big part of their job is understanding what AI risk is being introduced into the organization.
a lot of which is basically cyber risk.
So we're trying to create this portal where they can come in and view that more high level information, if you will, and not dive into the nuance of this is the defender alert or this is the insider risk alert, but they get that high level view.
Any questions?
Were you expecting to see anything in here that I did not show you that you think would be a gap that you think would be missing?
Mike Agar   48:55
Well, I mean, I wasn't expecting to see it, but it does, you know, the business side of the reporting, I guess, is what we're, is the gap we're trying to plug. And as I said, I didn't expect it to be here, but it kind of gets close to doing a lot of things, this, but it feels like it doesn't quite do those things fully.
Sourabh Sardesai   49:06
Yeah.
Mike Agar   49:14
you know, like the map you showed, that is a great visual, but then it doesn't include Foundry agents and it only shows connections, not really flow and throughput. So, you know, it feels like there's a lot here that in a year's time, it feels like this might sort of be more ready.
Maha AbuRumman   49:16
Yeah.
I would, yeah. Oh, sorry, I would say it's less than a year. You do see Foundry agents in the map, by the way.
Mike Agar   49:35
Oh, you do?
Maha AbuRumman   49:35
And yeah, yeah, and I can also see immediately one of them is risky because it's red.
Um, but I, you do see.
Mike Agar   49:42
but you don't see their connections.
Maha AbuRumman   49:45
Not, no. I actually don't know if there are any connexions between the ones that I have in this environment, but I'll double check.
Mike Agar   49:50
Yeah.
Pankaj Arora   49:55
I think what it doesn't give us is the internal workings of an agent.
and some kind of reporting and metrics on top of what that agent is actually doing. Is it doing it successfully? Is it failing over? Are there any exceptions?
Those kind of things.
Maha AbuRumman   50:10
So more like health metrics is what you're thinking and productivity metrics.
Pankaj Arora   50:15
I think productivity metrics, health metrics will usually just tell us whether it's awake and is receiving and responding, right?
Maha AbuRumman   50:16
Okay.
Mhm.
I can take that feedback, but can I maybe flip that a little bit?
Poorna Bavapalli   50:32
But.
Maha AbuRumman   50:33
How do you?
measure productivity from a Foundry agent versus a Copilot Studio agent versus a Service Now or a Salesforce agent. Like how do you provide consistent measures?
for agents built on different platforms with different tools.
Pankaj Arora   50:53
So every agent, I think in my opinion, every agent is built with a purpose, right? As long as it's fulfilling its purpose, 95% of the time, so whatever that threshold, we might configure it.
Maha AbuRumman   50:57
Yes.
Pankaj Arora   51:06
That probably tell us whether it's doing its job or not and how efficiently it's doing its job.
How often is it failing over? How often does it need to invoke maybe a human in the loop process?
Maha AbuRumman   51:12
Yeah, Bo.
Mhm.
Pankaj Arora   51:19
So those kind of things will probably create that kind of dashboard or some kind of a metric to tell us whether it's doing what it needs to do. And also sometimes maybe we have multiple agents working in conjunction to complete the workflow. But maybe four of the agents are actually very consistent work.
Maha AbuRumman   51:34
Yes.
Pankaj Arora   51:39
90% of the time, but there is one which lags and will be maybe has a 70% accuracy and because of that workflow, the entire, because of that one agent, the entire workflow actually has a drop in output. So those kind of things, how would we, I mean, where is that data we get to get it out of the system? I mean, I'm sure there is somewhere that.
Maha AbuRumman   51:50
fails more consistently.
Yeah.
Pankaj Arora   51:59
data and the stuff is logged. Or is it then becoming a developer or engineers problem that he must make sure in some way that this data is logged so we can then produce an output on it.
Maha AbuRumman   52:02
Mm.
Yeah, so currently that data is not in Agent 365. And I think a big part of the reason is kind of some of the questions that I'm asking you, right? Like how do we define, how do we define what is efficient? How do we define what is intended versus unintended human, the loop invocation, for example? How do we define accuracy? All of those things.
Poorna Bavapalli   52:24
You.
Maha AbuRumman   52:31
Now, I believe, and again, Vincent, please jump in and correct me, not my area of expertise, but with Foundry, you have some capabilities to trace and measure some of that. Same with Copilot Studio, you'll have capabilities to trace and manage some of that, essentially any dev platform.
Vincent Rouet   52:42
Yeah.
G.
Maha AbuRumman   52:50
One of the requirements that I'm raising on behalf of my other customers is being able to pull more telemetry into Agent 365.
Um, and...
keep this under NDA. I know with Agent 365, we're looking at integrations with OpenTel, so you can bring OpenTelemetry information into Agent 365 as well. So there is, there are plans, but like I don't know exactly like you wanted to.
but it is an area we're aware of.
Poorna Bavapalli   53:23
Or is it a requirement?
Maha AbuRumman   53:23
Sorry, Vincent, I spoke over there.
Poorna Bavapalli   53:25
No, no, I was just asking whether you got one question, Pankaj. Some of this could be a requirement for a Foundry developer, may not be a requirement for an agent to expire user as well, right? So is it like something we have differentiated those?
Pankaj Arora   53:42
No, I think we have overall requirement for every agent really. So the document that I've shared, that contains all of those requirements. And those requirements are for all agents, regardless of which platform they have been built on.
Vincent Rouet   53:56
Yeah.
Poorna Bavapalli   53:57
No, I get that. I think based on the user profile, the information what you want to look where is, isn't it?
Pankaj Arora   54:06
As long as it's an agent, we want it to report metrics. We want to know whether that agent...
Maha AbuRumman   54:06
So...
Pankaj Arora   54:11
I mean from a business perspective, if an agent has been billed and is billed to do something, we want to know how often is working and what's his success failure rate is and other metrics.
Vincent Rouet   54:21
But you get this level of, you get this level of monitoring at each control control plane or management planes of where that agent is running. So, Foundry will give you that observability. Copilot Studio will give you that observability. If you're running a few on Salesforce, they will be giving you that own monitoring platform as well.
Maha AbuRumman   54:23
So there.
Vincent Rouet   54:41
I hear your point that you might not want having to jump to all these different platforms to see, you know, what's going on with all these different agents. So some level of open telemetry, you know, we would want those platforms, those control planes to be able to extract some telemetry and build some sort of Power BI dashboards.
Right, this is sort of your one pane view to start with, right? Were you able to say, oh, that one looks red, but at some point you will have to go and dive on that red dot. It takes you to the Copilot Studio, it takes you to the Foundry observability panel where you can actually see the details of what's going wrong. So
Mike Agar   55:02
Yeah.
Yeah. And that's what it feels like. Agent 365 could be that front end that connects all of the data together and lets you drill down. And obviously you might disappear off into those systems. But that's what we're after is that front dashboard that we can give to both business users and technical users. They often want the same bits of information and then start to get into detail, right? Is it costing me too much? Is the cost trending upwards? So I need to go and look at it.
Vincent Rouet   55:22
Yeah.
Yeah.
Mike Agar   55:45
how is it performing compared to the last version? You know, we just changed the model that it's using behind the scenes. Has the accuracy gone up or down? All of these things we want to be able to report on. The data's there, I think, in the core systems, if you like, the foundry, etc., but it's bringing it together. And at the moment, this is just a, for me, this is a
Maha AbuRumman   55:53
Mhm.
Mike Agar   56:04
a governance layer around the agents, which is useful, but it's not that bringing together. It's not the kind of agent dashboard. It's an agent control plane, which I think is what you would, what you would say it is.
Maha AbuRumman   56:16
It's an agent control plane, yeah, but it is also, we'll be bringing in a lot of that. So these are some of the frontier public preview capabilities that are available today. So agents usage dashboard or agents usage reports might be worth looking into. It might not have everything you want. On the roadmap, we've got the FinOps and evaluations.
Mike Agar   56:18
Yeah.
Yep.
Maha AbuRumman   56:35
coming in. We've got data export coming in, but we've also got the support for baseline drift detection remediation on agents coming in as well. So these are some of the things that are currently in development. So I think you'll start to see more and more of what you're asking for. Again, I cannot commit to timelines, but
Mike Agar   56:50
Yeah.
Maha AbuRumman   56:55
Like I said, from the 1st of May to today, like this roadmap has changed on an almost daily basis.
Mike Agar   57:04
So if you can send this through, if there is any timeline information, because I guess we're going to have to make a decision, right, whether we build this ourselves or wait. So if there's anything that could help us make that.
Maha AbuRumman   57:04
Ha.
Yep.
I will.
I will need to cheque if I can share this. To be honest, like I said, it is subject to NDA. I show it to you, but I don't know if I can send it to you. So I'll need to cheque that. But yeah, like just to let you know, again, like from the 1st of May, it went live with whatever was on here, but everything that says updates are things that were kind of built in since it went GA and.
Mike Agar   57:20
Yeah, yeah, yeah, yeah.
Oh, I see.
OK.
Yeah.
Maha AbuRumman   57:38
immediately released into GA as well. So that's how quickly things are moving on all of them.
Mike Agar   57:42
Okay, okay.
Maha AbuRumman   57:44
Um, conscious of the time, any, yeah.
Mike Agar   57:45
But.
Yeah, and I did, I did, we wanted to talk about DBs in this session as well, so we're almost out of time for that, really. Is there any key questions left on this?
If you can send through what you can, Maha, that would be helpful because the deck looked really good, right? And would be useful to have. If there's any more timeline questions that you are able to suggest anything to, even if it's informally or whatever, that would be helpful. We don't need everyone for this, but I don't know, Vincent, the DB.
Maha AbuRumman   58:01
Yeah.
Yeah.
Yep.
Mike Agar   58:17
type questions is that is that one with you and Alex and Sarah Pankaj and you know basically who whoever wants to stay behind if people can hang on just for a little bit we might be able to cover that off.
Poorna Bavapalli   58:30
I have an half-top at three.
Vincent Rouet   58:30
Yeah, I would.
Maha AbuRumman   58:30
I think, yeah, Gemma and I will have to drop. So thank you.
Vincent Rouet   58:34
I can stay and see, see, hear those questions, yeah.
Mike Agar   58:34
Thank you very much, Dan.
Poorna Bavapalli   58:35
Okay.
Yeah, if you can share the context, Mark, I think having some query there.
Mike Agar   58:41
Cool. Do you want me to give context, Alex, or did you want me to just hand over to you?
Poorna Bavapalli   58:46
Thanks, Vincent. Thanks.
Alex Hill   58:48
Um...
Vincent Rouet   58:48
Thank you.
Alex Hill   58:51
Yeah, I'm having free to give context, like it's...
Mike Agar   58:53
Okay.
So, basically, Vincent, we we we we're building agents.
Alex Hill   58:55
Okay.
Vincent Rouet   58:59
Yeah.
Mike Agar   58:59
Those agents are going to have...
an operational data store is the best way I can think to phrase it. But as the agent is doing stuff, and it might not even be an agent, it might be an orchestrator process that's running that then uses agents. But essentially, when we're building an AIAgentHelpdesk solution to a problem, we're going to need to manage state in that process, right? And we're going to need to output some kind of log that says, you know, I've done step one, it's now with the user to confirm
X, Y, and Z, and then it sort of might wait, and then the user responds and something happened, and basically it's logging state outputs, et cetera, to some kind of database.
Vincent Rouet   59:40
Yeah, OK.
Mike Agar   59:41
Now, it's that question that we're looking at, right? What is the database? Should we have one per use case or one generic database that we put things in? And then where should that database be? Should that be an SQL? Should it be Postgres, just it hosted in Azure? Or the big question is, should we just put that straight into Fabric?
i.e. it's a fabric database that we're using to host that production type data. And we're leaning at the moment towards a fabric answer, probably fabric SQL, Alex, unless that's changed. But that, I guess, is the question, right? Where do we put it? And do we have one or many?
Vincent Rouet   1:00:02
Up.
Alex Hill   1:00:14
Yeah.
Mike Agar   1:00:19
and is fabric the right place?
Vincent Rouet   1:00:22
OK, I'm trying to, I think I'm trying to think that fabric is more of a data, you know, it's sort of your one leg, right? So, unless that data is specifically being used for reporting on on some some sort of monitoring on some some reporting on performance.
you know, or whether, as you said, this is really just a database to capture, okay, I've done this state, now, you know, I'll remember that I've responded to that e-mail, we now responded to the answer from the user. So this is just a log of activity. So this is more like transactional and an operation point of view.
I'm thinking that that's usually better if it's closer to the workload, i.e. in a Cosmos DB. I think the SQL or Cosmos, I think the Cosmos side of thing is, you know, how you can store, it's a non-relational database, so it's very often very popular with, I just want to be able to, you know, I've got a...
an agent's been running, he's a jason snapshot of all the states of my process. You know, it's easy to remember and just dump it into a Cosmos DB so I can rehydrate when the process restarts. So Cosmos DB is quite popular for that purpose. Then if it's a relational SQL or
or Postgres is really down to the preferences for the development team. You know, I see Postgres being very popular because new generation of developers, personally, have used SQL myself a lot. So already I'm thinking, you know, the database used specifically for that workflow.
Close to the workloads, it almost needs to be deployed as part of that package. Now, if you want to be able to report on say, so say you're using one same schema to to log all the different steps going on in your in your in your multi-agent workflow, your.
You're probably thinking workflow that couldn't be mixing, you know, deterministic and non-deterministic steps, so this might be logged into Cosmos or PostgreSQL. Now, if you want to...
You know that anyone right into your OneLake, push some data into the OneLake, so you could do some Power BI there, but I'm not really imagining having a live system that's gonna want to go and connect to a database in Fabric.
Mike Agar   1:02:42
Yeah.
Vincent Rouet   1:02:55
It has to be as low latency as closer to the workload, and also being able to deploy as part of the same life cycle, really.
Alex Hill   1:03:06
Two.
Mike Agar   1:03:06
But why, Vincent? Because I, in my head, when Alex was first talking to me about this, I said exactly the same thing. And then, and then I started to wonder, well, is Fabric any slower? Is the latency any lower? If it's in Fabric already, is it easier to get the reporting data out from Fabric, right? You've kind of already got it there. You'd have to be careful about.
Vincent Rouet   1:03:07
Yeah.
Mike Agar   1:03:24
you know, reporting from the same production database as you have operational systems writing to, but you know, what, why not?
Vincent Rouet   1:03:30
So...
Okay, so let's now think about latency, right? In this day and age, we've got light speed connexions between systems, right? So I think for me, it's more in terms of boundaries, you know, ownership, separation of concern in between, you know, I'm building solution in HR, I've got business processes in HR, I'm logging, you know, it might be I've got specific.
Mike Agar   1:03:39
K.
Vincent Rouet   1:03:54
constraint on my own in terms of logging, making sure we don't have any PIA data. Therefore, my database schema is going to be pretty much my own definition of it. I will open the gate to, you know, the analytics teams who want to come and read some data from our agents processing. Therefore, they might be.
Thing fabric, there's this view, you know, you can.
Review of table right, copy the data, so that that would be that would be the approach, but I think this is for me spending, I'm always thinking life cycle management of those artefacts and and who owns it, and and if you want velocity and protection, it's better if it's close to.
Ultimately, the decisions on a budget.
Right, so yeah, it's not so much from a technology or latency point of view. You're right to correct me here.
Mike Agar   1:04:50
Um...
Vincent Rouet   1:04:50
So, yeah, and yeah, and Cosmos being quite, I mean, and again, I'm not sure whether might you've got all those world war requirements. Cosmos is very often very popular when you want to be able to replicate the state, you know, say you've got a process starting in the MEA, but it's going to be picked up by an agent running in Australia. Therefore,
you might want to have that replications of the state instantaneously. I don't know, do you have this sort of requirements? Are the geo-localizations of agent of processes running, right? If that's a question, Cosmos DB is a good candidate for that.
Nick Brooker   1:05:29
I think we said depending on the payload, it depends on what system we were going to go forward, didn't it? Cosmos, though, again, you've got the ability to create a Cosmos database in Fabric, haven't you?
Mike Agar   1:05:30
Big.
Vincent Rouet   1:05:46
Okay, yeah, I'm not I'm not professional enough on fabric. That's interesting. I can look this up, yeah.
Nick Brooker   1:05:54
I think you can create a Cosmos database in Ferreira. So what we recommended is depending on the payload, if it was more telemetry, then we were, we sort of recommended KQL and putting it in the Custo DB. If it was transactional, then SQL was kind of the platform of choice just for the flexibility of everybody that were working on it.
there to work more with SQL. It was in Fabric. It seemed like a relatively simple solution. I'm not against Cosmos, to be honest either. We can.
I think it's kind of what we were talking about is kind of having that decision tree, weren't we? What makes it go on to...
Cosmos, SQL, or KQL.
Vincent Rouet   1:06:35
Well, you know, our KQL, yeah, this is really for high streaming of, this is really good for telemetry, your logging. I think you're expecting more to write to it and then read at a later stage. I think if I was developing a workflow, let's say in the logic apps, if I had to go and write some KQL to go and read the state of my process in a KQL.
Nick Brooker   1:06:46
Mhm.
Vincent Rouet   1:06:58
I'd probably rather do that with a SQL statement, right? So I think, yeah, because in fact all that open telemetry and everything is going into Azure Monitor, up inside, this is all KQL.
Nick Brooker   1:07:02
Ha.
Vincent Rouet   1:07:13
Um...
You know, I think what I, I mean, I've been building a lot of workflows and every time, you know, you're generating a state where you've got that structured status of a message where you receive an e-mail. So very often the output of the e-mail is going to be a jason format. And I find it a lot easier.
to save it into a Cosmos database than having to, I mean, I can always store it in a role in a SQL role or BLOB storage. I think that's fine.
I guess the one of the consideration probably to give is how do you store when you've got those workflows, those, you know, processes leaving, how do you store these structured contents such as JSONs or less and less XML, but those jason format? What is the best? Where do you store that?
So I think the question would be, yeah, so I'm building a logic apps and I've got a process where I'm at a state where users responded to an e-mail, in the e-mail there was an attachment. So there's a base 64 content of that attachment. I want to snapshot this state because it might be resuming in two weeks time.
Where, where do I store this?
Mike Agar   1:08:33
Pankaj, Sourabh, is that a question for you guys? If you were building an application that did this today, what would you do? Because presumably today you wouldn't go to the data team and ask them for a fabric capacity, right? You'd spin something up.
Sourabh Sardesai   1:08:42
Yeah.
Yeah, yeah, so...
Pankaj Arora   1:08:46
So, for AI observability, the so far we have what have we have been doing is we are writing to application insight and from application insight the data goes into BLOB after whatever time is set, but we don't we don't actually have any dashboards and importing kind of things on top of it, unless we've custom built.
Mike Agar   1:08:59
But I guess it.
If you were building a logic, forget the AI thing for a second, if you were building a logic app that did a business process, and as part of that, at some stage, you wanted to log some states, right, or some steps and like store the fact that state step 2 went well.
Sourabh Sardesai   1:09:06
Burt.
Self.
Francisco Cachado   1:09:18
Ha.
Yeah, exactly. Like, I go more for what Mike just said. Like, we, like, the fabric will be good for the application insights, but like what we care more now is operational data. We want to store the agent states, the workflow runs, what is the status, what we send to the customers and so on.
Mike Agar   1:09:20
What are you doing?
Sourabh Sardesai   1:09:21
Thank you.
Okay.
Francisco Cachado   1:09:39
So I need to have an operational database, not so much for the logging is also important, but to have operational data stored somewhere.
Sourabh Sardesai   1:09:45
Yeah.
I need this.
Yeah, something similar to functional logging and then the options like probably no SQL like Cosmos or SQL database or Postgres, these will be options.
Vincent Rouet   1:10:00
Right.
So in any workflow, you've got the telemetry from the actual run times, right? So what's going on at every step, that's fine, that's app insights. And then you've got this business activity monitoring, let's call it that way, where you're actually storing the content of that e-mail, the response that you send, that type of thing. So.
Mike Agar   1:10:10
Yeah.
Vincent Rouet   1:10:21
I think that's what we're talking about here, right? So...
Mike Agar   1:10:23
Yeah.
Vincent Rouet   1:10:25
When I get the question, it's fine to send that to a role in a SQL database. I personally prefer to store it as a snapshot. It's easier to rehydrate and work with in our Cosmos database, so...
Mike Agar   1:10:38
I think the first question is, should the database that we're spinning up be in fabric or not? The second question is, what type of database should it be? And the third question is, should we have one database that everyone shares for all of these different agentic use cases, or should every agentic use case spin up whatever the hell they want individually?
They're the three questions I guess that I've got to give to, you know, that I want to kind of try and answer between us all.
Alex Hill   1:11:01
Ha.
Yeah, I think one of the concerns that we had, Mike, with each AIAgentHelpdesk solution spinning up its own.
storage was that we would end up with multiple 10s, if not hundreds, maybe thousands. If we went for a Cosmos solution, so a NoSQL solution, that might mitigate
Mike Agar   1:11:21
I agree.
Alex Hill   1:11:33
The issue around each.
Agentic system, being its own schema, would they then will be able to?
store their data in the single Cosmos storage instance.
Yeah.
Vincent Rouet   1:11:56
OK, so should we should we leave it to the transcript? I think we've you've explained the question mark, so the transcript will pick up, we will have those open questions, suggest I can consult internally, and then we can maybe follow up on that. Yeah, yeah.
Mike Agar   1:12:11
Okay.
Okay.
Alex Hill   1:12:14
Okay.
Mike Agar   1:12:15
Yep.
Vincent Rouet   1:12:16
But yeah.
But I, yeah, I see what you mean, you...
Mike Agar   1:12:19
I think your guidance there, Vincent, I think at the beginning you were saying fabric maybe not, but largely due to kind of segregation of responsibility. Does it make sense that your data layer is kind of becoming part of your operational function?
Vincent Rouet   1:12:28
Yeah, that, that's that.
I would stay on that statement personally, yeah, for my personal opinion. It's fine to copy that data into Fabric for reporting purposes, but just for the operational, you would want isolation. So, and it seems to be a bigger culture around SQL probably on your side, so maybe SQL would be a good place. So,
App analytics, monitoring, like you're already using for the telemetry, block storage and SQL for business, business activity monitoring, you know, storing those business specific artefacts and copying into fabric, not copying, but right from fabric.
Mike Agar   1:12:57
Yep.
Yeah, yeah, yeah, yeah.
Vincent Rouet   1:13:12
Now, in terms of how many instances, yes, are we going to have thousands of SQL Server of Azure SQL all over the place? Maybe there's a question there to analyse as to how your teams are managed, how your development teams are organized, say Pankaj and Francisco, you bought.
Building 2 solutions, should they be sharing the same database, or that's, yeah, maybe that's a question.
Alex Hill   1:13:39
Is it easier to share a database if they work with Cosmos over Postgres, for instance?
Vincent Rouet   1:13:46
thing is the same. You got some point up to create your own database and yeah, decide to use it. But you have to be added as a user.
Alex Hill   1:13:48
Is it?
Vincent Rouet   1:13:58
I think on that last point, how many do we create? Maybe that's someone what question I can get back to you.
Alex Hill   1:13:58
It just went from a...
Mike Agar   1:14:04
Maybe it's one by domain, right? Maybe it's we should have one for HR and mirror the foundry structure that we think we're going to be creating.
Vincent Rouet   1:14:06
Yeah.
Yeah, because you might want to create an API. So at one point you create a database and then you create an API that you expose and every new workflow that you start creating, you use those API. So as opposed to directly using the SQL connector, you just...
post that status to a REST API. So I think you could have a developer who looks after this tracking database, looks maintain those the REST API, and then now every developer knows that, you know, whenever they need to store, snapshot the status of a process, they can just call that, dump that data to a REST API.
That could be an approach.
Mike Agar   1:14:57
Okay.
All right, so thank you, Vincent. That's useful. If you can take those questions away and if there's any kind of more...
Vincent Rouet   1:14:59
I hope that answers some of your question.
Mike Agar   1:15:06
you know, detailed answer or formal answer, then that would be good. But I think we've, there's some fairly helpful guidance there.
Vincent Rouet   1:15:09
Sure.
Mike Agar   1:15:15
Is there anything else, Nick, Alex, that you want to...
Vincent Rouet   1:15:15
Okay.
Mike Agar   1:15:19
Raise here.
Alex Hill   1:15:21
I think that's been really helpful.
You can take that whatever, yeah.
Mike Agar   1:15:33
If there's any follow up questions, guys, just drop it into this meeting chat. You know, you can tag Vincent in if just to make sure it pops up, hopefully and notifies him. But you know, if there's any follow-ups, we can put it in the meeting chat. Okay.
Alex Hill   1:15:36
Mhm.
Vincent Rouet   1:15:46
Okay.
Mike Agar   1:15:48
All right, thank you very much. Sorry for running guys, but appreciate appreciate you your time. Thank you very much.
Vincent Rouet   1:15:48
Thank you. Thank you.
Pankaj Arora   1:15:49
You.
Vincent Rouet   1:15:51
Yeah.
Alex Hill   1:15:52
I see. Cheers. Goodbye.
Vincent Rouet   1:15:53
Thank you. Bye-bye.
621792274320
Mike Agar stopped transcription

