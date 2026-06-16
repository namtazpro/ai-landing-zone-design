# Microsoft Support - Foundry platform and MCP servers 22 may 2026

_Extracted from Microsoft Support - Foundry platform and MCP servers 22 may 2026.docx_

---

Microsoft Support - Foundry platform and MCP servers-20260522_140016UTC-Meeting Recording
22 May 2026, 02:00pm
1h 22m 55s
576072292608
Francisco Cachado   0:27
Hello, everyone.
576072292608
John Blog   0:30
Hello, good afternoon.
576072292608
Sanjay Sardesai   0:31
Hello.
576072292608
Jordan Watkins   0:32
Hello, afternoon all.
576072292608
Francisco Cachado   0:33
Good afternoon.
Some of you already have a few meetings this morning.
576072292608
Sanjay Sardesai   0:44
Too many meetings.
576072292608
Francisco Cachado   0:47
Jacob Phan.
576072292608
John Blog   0:47
Too many meetings, yeah, exactly.
Okay.
576072292608
Francisco Cachado   1:10
So, with the, we still missing, we are waiting for someone else, Jane Star John Blog, do you know?
576072292608
John Blog   1:11
Okay.
I think Jacob Phan was going to join. I was going to say George Smith, but George Smith is here.
576072292608
George Smith   1:23
Hello.
576072292608
John Blog   1:23
Yeah, hello, George Smith.
576072292608
Jane Star   1:26
Yeah.
576072292608
George Smith   1:27
Do we have everyone? Well, we don't have...
I don't have Jacob Phan.
And I didn't get a response from Jacob Phan.
576072292608
John Blog   1:39
Well, he was out of office.
Now he's back online.
576072292608
George Smith   1:54
You are the sole representative from Microsoft, John Blog, so we're going to put you on the spot now, by the sounds of it.
576072292608
Jane Star   1:57
Jacob Phan.
576072292608
John Blog   1:57
If.
576072292608
Jane Star   1:58
Hitesh.
576072292608
John Blog   1:59
Jacob Phan.
Yeah.
I am.
Okay, I think we had quite a...
Agreed on specific focus for this afternoon, right?
576072292608
Jane Star   2:16
Yup, yeah, George Smith, you go.
576072292608
George Smith   2:16
So...
576072292608
John Blog   2:17
On the foundry.
576072292608
Sanjay Sardesai   2:18
Yeah, so.
576072292608
George Smith   2:18
Well, yeah, I mean, I'll hand over to you as quickly as I can, Jane Star, really, because you're probably better to explain what the focus is. But the idea of the meeting really, I think, was fundamentally Foundry.
576072292608
Jane Star   2:24
Mhm.
576072292608
George Smith   2:30
How are we doing in MCP servers? Are we having lots or fewer? Is it one API per server, et cetera? MCP versus toolbox. And then within Foundry, how are we structuring agents within Foundry specifically about domains, which I think might be more what you might be able to help us with, John Blog. So maybe we can at least.
576072292608
John Blog   2:45
Yeah, so that will be my part. How I could join Gemma on the MMC. Yeah.
576072292608
George Smith   2:52
If we can at least start with that bit then and see whether we can make progress with you on the domain part, Jane Star. But I guess I'll hand over to you, Jane Star, to kind of.
talk about what you want to get out of this and get us started if we can with just John Blog.
576072292608
Jane Star   3:06
Yeah, for me, for the goal of SCOE this week, I really want to get the approach on tool registry and MCP aligned like by today. But I mean, if John Blog's special expertise is in segregation, then by all means we should start there. So.
John Blog, let us know which topic you think you can provide us more guidance on.
576072292608
John Blog   3:30
Yeah.
Okay, let me just see if he had accepted the call.
576072292608
George Smith   3:39
He hasn't accepted this one now, I've got no response from her.
576072292608
John Blog   3:45
Awan.
576072292608
Jane Star   3:49
No worries, like John Blog, if you want to start with segregation, and that's the area that you have more focus on, you can start there.
576072292608
John Blog   3:51
Yeah.
576072292608
Francisco Cachado   3:54
Yep.
576072292608
George Smith   3:56
Ohh, this may sound.
576072292608
Jane Star   4:00
Oh, okay, okay, awesome. All right, let's talk about MCP then. Jacob Phan Jacob Phan.
576072292608
John Blog   4:03
Okay.
Jacob Phan, just thank you for.
joining. Yeah, we were just going through both the agenda for today, and I think the main interest seems to be around the MCP conversation. So I think that's what Jane Star would like to get clarity on. So how if you're
576072292608
Jane Star   4:21
Mhm.
Sure.
Yeah, I can, I can give an intro on how currently we are thinking about MCP, like from McKenzie and, and then Sarah, Pankaj, George Smith, Jordan, feel free to voice your opinion as well, and then, of course, Jacob Phan and John Blog keep us chat dot what we discussed is the best practice. Also, I want to hear you guys.
576072292608
John Blog   4:30
If you can start.
576072292608
Jane Star   4:49
Um, what's the best way to do this? Um, so let me...
576072292608
George Smith   4:52
Is that okay, John Blog? Sorry, I realize. Oh, you've just joined and you're being sort of pounced on. Are we all good? Happy with that?
576072292608
Jane Star   4:58
Hmm.
576072292608
Jacob Phan   4:59
Jacob Phan.
Let's see how far do I get.
576072292608
George Smith   5:02
Okay.
576072292608
John Blog   5:03
Yeah.
576072292608
Jacob Phan   5:04
Jacob Phan.
576072292608
Francisco Cachado   5:04
Yes.
576072292608
George Smith   5:05
Going in a minute.
576072292608
Jane Star   5:05
Okay, yeah, let me share my screen. So still back to the same same slide. And here I put a giant yellow sticky here to just like pan down our current thought about two definition registry. So what we propose and we think is the best way is.
576072292608
George Smith   5:11
Ohh, I guess recordings on.
576072292608
Jane Star   5:27
We think the tools should be categorised and then grouped first, instead of like leaving them as individual. And I like always assign individual tools to agents because that's just very context intensive. And we also envision in the future, right, like.
Contoso will have a lot of agents with a lot of tools and we will want a way to systemize, categorise those tools. And after we do the categorization, the group of tools should be wrapped as FCP server so that we can leverage the benefits of MCP, right? For example, like the tool functionality will be better described to the agent.
there is input validation, the tools will be dynamically exposed to the agent. Like also like, yes.
576072292608
Sanjay Sardesai   6:20
But.
Yeah, yeah. I also would like to add one point is we would like to create MCP servers, yes, if required, if it makes sense. But let's say if there are some tools which are supposed to be isolated and more sensitive, and that I think we should also define a way to keep them isolated.
576072292608
Jane Star   6:23
Mhm.
Mhm.
576072292608
Sanjay Sardesai   6:42
and not put it into any MCP server and then just expose it via open API spec, if within the tool set, of course.
576072292608
George Smith   6:50
They should always be MCP exposed, Sarah, right? We want to use MCP always, even if they're on their own MCP server so that they're totally isolated. You'd still want them exposed via MCP, wouldn't you?
576072292608
Jane Star   6:51
Yes.
Yeah.
576072292608
Francisco Cachado   6:59
Yeah.
576072292608
Sanjay Sardesai   7:00
So, for example, I'll give an example of what I wanted to say. So, for example, there's an agent, yeah. Let's say, let's take an example of Barry, yeah, and then there is an MCP server for all the Maximo tools there. OK, now let's say if Barry is exposed, it's connected to MCP Maximo MCP server.
Barry gets context of all the APIs within the maximum.
By default, yeah.
576072292608
Jane Star   7:26
There is a way that we can control, like there's an attribute in the MCP whereby you can say allow tools and you only specify like in this MCP server, only this list of tools can be seen by this agent.
576072292608
Francisco Cachado   7:26
Jacob Phan.
576072292608
Sanjay Sardesai   7:39
Exactly.
But then again, what we'll do, what we'll end up with is like, okay, now there is a Maximo MCP server with only five APIs within it. Let's say if you have to use the other five APIs within the same thing, that's again a problem. You'll have to create another MCP server for Maximo with those five tools.
576072292608
Francisco Cachado   7:41
Yeah.
576072292608
Sanjay Sardesai   8:00
Right.
576072292608
Jane Star   8:01
No, the approach should be you put all the Maximal tools, but if you, if we think that's a group, like let's say it's a group that we think correct, is you put all the Maximal tools behind the same MCP server, but when you give the agent that MCP server, there's an attribute for you to say.
This agent B only has list 2 ABC out of this MCP server, but not everything.
576072292608
Francisco Cachado   8:27
Yeah.
576072292608
Jane Star   8:27
But there's an attribute you can specify there.
576072292608
Sanjay Sardesai   8:31
Okay, and then we can find.
576072292608
Francisco Cachado   8:31
And we just like when did we just expose the necessary tools from that server to that agent and not the full thing because that's fully beyond sort of regarding like containerized, like separate by scope, each MCP, don't put everything in the same MCP, have MCP specific for each type of action, but then...
As I may say, like, we then separate which tools are exposed to each agent.
576072292608
Sanjay Sardesai   8:59
But, OK, and where do we set that? Where do we keep that configuration?
576072292608
Jane Star   9:05
That configuration, for example, in Foundry SDK, right, like this syntax for MCP tool, where you need, where it needs an argument as the MCP server endpoint, and it also has an argument to say, allow tools, which is a list.
576072292608
Sanjay Sardesai   9:23
So for example, if I'm creating a new agent, I have a MCP server for Maximo. Is it something I want to create, something similar to Barry, for example? Then how will I then choose, if I have to connect to MCP server, who will then determine that agent will get these tools of access? Who's going to be the admin of that?
576072292608
Jane Star   9:32
Mhm.
Yes.
Mhm.
576072292608
Sanjay Sardesai   9:45
Yeah, Jacob Phan.
576072292608
Jane Star   9:45
Yes.
576072292608
Jacob Phan   9:48
No, no, no, I let the answer. My points are different. That's why I raised my hand.
576072292608
Sanjay Sardesai   9:53
Okay, good. Sorry. Jane Star here. Sorry, I cut you.
576072292608
Jane Star   9:54
Okay.
No, no, Jacob Phan, go ahead.
Those are all here.
Ohh.
Jacob Phan.
576072292608
Jacob Phan   10:05
Just clarify this. So we're talking about a slight different thing here, I think. So LLM got function calling or tool calling. So we know that. And then MMC, I think, operates slightly different where MMC operate on the kind of a client server, which is effectively a client can use multiple model.
Right, rather than just, just, just, just one model. So, I think when you say tool definition here, what did you mean by that? Is that tool here mean, mean because within MMC specification server is also exposed that.
that tool calling as well. So maybe before I make my recommendation or my comment, can I just be sure to definition, what does that mean?
Is that an API? How does that define?
576072292608
Jane Star   11:06
It can be an API or it can also be a simple function that performs some deterministic task, for example. And our vision is like we will use fast MMC to wrap up.
576072292608
Jacob Phan   11:15
Okay.
576072292608
Jane Star   11:24
outside of like as a API or a function that we want to give to the agent and let it to use where everything is needed.
576072292608
Jacob Phan   11:26
Mhm.
Mm.
576072292608
Jane Star   11:36
Does this answer your question?
576072292608
Jacob Phan   11:39
Okay, cool. So I think very briefly we touch on the other day, I think it's Tuesday, I can't remember, but so is that the approach is to effectively one-to-one relationship between the open API endpoint to calling? Is that what we're suggesting?
576072292608
Jane Star   11:43
Mhm.
No, I know right now in MIT, we have some tools like in APP. But moving forward, we might have, like we might build additional tools whereby we want to put a group of tools behind the MMC server.
576072292608
Francisco Cachado   12:08
Mm-hmm.
576072292608
Jane Star   12:21
Instead of by putting each tool as a separate, uh, as a separate one in APP.
576072292608
Sanjay Sardesai   12:27
I think of Jane Star.
576072292608
Jacob Phan   12:28
Ohh, what?
576072292608
Jane Star   12:29
Mhm.
576072292608
Sanjay Sardesai   12:30
Sorry, the other day we agreed right that every tool is going to be a API. Every tool is going to be an APP.
576072292608
Pankaj Arora   12:37
So, can I interrupt?
576072292608
Jane Star   12:38
Okay.
Yep.
576072292608
Pankaj Arora   12:42
Just to just to clarify what we want to do.
uh in this area is
What we currently have is our backend system exposed via APIs, via Azure APP, Azure API management, right? That's what currently is that exists.
576072292608
Francisco Cachado   13:00
Mhm.
576072292608
Jacob Phan   13:00
Right.
576072292608
Pankaj Arora   13:03
in our environment.
For autonomous agents, what we want to do is we want to use the same APIs and expose via primary toolbox.
576072292608
Jacob Phan   13:12
Mm-hmm.
576072292608
Pankaj Arora   13:13
So, foundry tool books will give us an MCP kind of an endpoint, right?
576072292608
Jacob Phan   13:17
Mhm.
576072292608
Pankaj Arora   13:18
And in ideal world, agents should be using toolbooks to connect to those tools.
576072292608
Jacob Phan   13:23
Jacob Phan.
Yeah.
576072292608
Pankaj Arora   13:26
But that's the ideal picture that we want to achieve.
576072292608
Jacob Phan   13:28
OK, right.
576072292608
Pankaj Arora   13:30
And we don't, I don't think we want we want our agents to directly call APIs.
It probably, I think the best way is to have APIs wrapped into MCP UI toolbox, and then agent knows which tool it needs to call when in the process. And the agent can autonomously decide when it needs to create SR or when it needs to query SR.
576072292608
Jacob Phan   13:56
Okay.
576072292608
Pankaj Arora   13:57
Except for scenarios where, for example, we have a workflow. And in the workflow, we determine that there is a deterministic step, which we are very clear of that we need to do. So for example, when a user logs in, the first step before we start having a conversation with the user is to find out and identify who that user is and does that user exist in our system.
For an example, let's say based on e-mail address. So that's a very deterministic step that we need to do that the agent doesn't really need to be enrolled here. And in that scenario, maybe we can call an API directly. Does that make sense to everyone?
576072292608
Jacob Phan   14:21
Mm.
Jacob Phan.
That makes sense. So I think if I can summarise correctly, there are three points here. So the first point is we planning to expose the API endpoint as MCP server using things like APP. The second thing is we prefer to expose to the agent using MMC protocol as much as possible.
576072292608
Francisco Cachado   14:51
Mhm.
576072292608
Jacob Phan   15:00
And then the third point is for the non-deterministic, for the deterministic work, we might not decide to using MCP or expose a tool calling. Did I capture that three-point correctly?
576072292608
Francisco Cachado   15:00
Mhm.
576072292608
Pankaj Arora   15:13
Yes, I think so. Am I right?
576072292608
Jacob Phan   15:14
Okay.
576072292608
Jane Star   15:17
Oh, I don't quite get the last point, but I agree with the first two.
576072292608
Jacob Phan   15:21
Okay, so the last point, what I thinking was a for the deterministic workflow, we're not going to implementing as MCP tool if that's what I'm getting. So I just want to make sure that's correct or not.
576072292608
Jane Star   15:32
Um...
576072292608
Pankaj Arora   15:34
Yeah, so what we are saying is for deterministic step, Jane Star, when we are doing a workflow, we can call directly the API. We don't have to create an MCP server for those APIs.
576072292608
Jane Star   15:35
Okay, babe.
But we shouldn't have a workflow as a tool in the 1st place.
576072292608
Jacob Phan   15:48
Okay.
576072292608
Jane Star   15:53
So, I know this is how Barry is currently being built, but, like, based on our new design principle, like, we, we wouldn't have this case, like, that's all I'm saying.
576072292608
Pankaj Arora   16:04
Yes, so I'm not thinking just for Barry here. So I'm putting my AICOE hat on and I'm thinking beyond Barry, so across all the projects. So we're thinking probably a level above Barry and so.
576072292608
Jane Star   16:20
Yeah, that's fine. That's so for oops.
576072292608
Pankaj Arora   16:21
Yeah.
576072292608
George Smith   16:24
I've just stolen the screen.
576072292608
Jane Star   16:26
Jacob Phan.
576072292608
George Smith   16:27
And I've dared to try and draw a picture to try and explain what I think people are talking about at risk of being horrendously wrong. But...
576072292608
Francisco Cachado   16:28
Yeah, like...
576072292608
John Blog   16:33
I was going to try to draw as well. Go on.
576072292608
George Smith   16:35
Okay. So I think we've got an orchestration layer, right, which is running somewhere, ADF logic apps, whatever, right? So we've got an orchestration layer. That's not the subject of this conversation. We've then got an agent, which is part of this orchestrated process. And we might have many agents, but in this case, let's say we've just got one. That agent needs to be able to access many tools. Now, those tools might be an API call through to Maximo.
which would be exposed through Azure Integration Services. It might be into another system like Workplace Plus, which would also be exposed through this. We might have other systems with other middleware that, you know, SAP uses CPI, right? So we've got all of these APIs that we want to expose through MCP so that they are discoverable by the AI, which makes me slightly worried about, Jane Star, what you said with
576072292608
Pankaj Arora   17:05
Right.
576072292608
Francisco Cachado   17:09
Mhm.
576072292608
George Smith   17:18
attributes, turning them on and off, right? I thought the point or part of the point of MCP was that it's discoverable. But anyway, so we want to expose these things. And as far as I'm concerned, these are all tools, right? Be they API calls or a deterministic function that the agent can use that does something or decides something. I would have thought all of those things would be consumed via MCP.
576072292608
Francisco Cachado   17:33
Yeah.
Yep.
576072292608
Jane Star   17:39
I actually agree with you, like, yeah.
576072292608
Francisco Cachado   17:41
Yeah, this, this is, yeah, this is our ideas, like, even if it's a deterministic step or not, it's under an MCP, like, first of, like, all the tools represented in the same way, and then what is behind the the group, basically, what is making it work, the engine, it can be deterministic, so it can be an LLM call.
576072292608
Jacob Phan   17:47
Mm.
576072292608
Francisco Cachado   18:00
Whatever it, whatever it is in the inside.
576072292608
Jane Star   18:03
But yeah, and also even going back to the definition that Sanjay was mentioning, even when we define all the tools to be an API, what we want to propose is like those APIs in APP should be also wrapped in MCP server to just like.
rip the benefit of MCP as a best way to expose tools to agent.
Do we align on that front? And I also know, like Pankaj, your point is on top of all these four MCP boxes, we will have a Foundry toolbox, so that that's like a MCP gateway.
576072292608
Jacob Phan   18:30
Jacob Phan.
576072292608
George Smith   18:41
Yeah.
576072292608
Jane Star   18:45
To agent, and that I agree with you, so we will use toolbox as an additional layer, yeah, across as a MCP server gateway, but I think let me just cheque with Pankaj and Sanjay for the part that we want the API APP to be wrapped.
576072292608
Francisco Cachado   18:50
What?
Yeah.
576072292608
Jane Star   19:07
as MCPU server, do you guys agree or what was your thoughts?
576072292608
Jacob Phan   19:13
Yeah, so can I just come back on that three-point? And my comment, I agree on one of the point was group everything, Expo, tooling, via MCP protocol, adopt that as a way to standardise how you view the agent. I agree with that point. The other two point, I think my comment is the first one is.
576072292608
Jane Star   19:16
Mhm.
Mhm.
576072292608
Jacob Phan   19:35
I think that let's talk about deterministic versus non-deterministic. I think even on the deterministic way, or determinate process, that can be modelled as a tool within MCPs anyway. So for example, a tool could be calculated VAT. The calculated VAT is a deterministic process.
576072292608
Jane Star   19:49
Yeah.
576072292608
Francisco Cachado   19:51
Mhm.
576072292608
Jacob Phan   19:54
but then you can using MCP expose as a tool and then the agent can use that, right? So that, I think that makes sense. So I think I'll favour that. The last point I think we touched on the other day was Expo open API endpoint as an MCP tooling, kind of a one-to-one relationship. So actually I prep.
576072292608
Francisco Cachado   19:54
Mm.
576072292608
Jane Star   20:00
Thank you.
576072292608
Francisco Cachado   20:02
Mm.
576072292608
Jacob Phan   20:14
some slide here and I want to present it to get your thought.
Not sure we can see it. I'm sorry, I hijacked George Smith for a bit. Your diagram is better than me.
576072292608
Jane Star   20:25
Yeah.
576072292608
George Smith   20:25
Yeah, that's alright.
Jacob Phan.
576072292608
Jacob Phan   20:30
Okay, so I think, to be fair, I think Microsoft, taking my Microsoft hats for a bit, we do kind of send that message across. Oh yeah, it's very easy for you to explore open API endpoint as an MCP server. And our tooling do support that, APP do that.
576072292608
Jane Star   20:39
Mm.
576072292608
Jacob Phan   20:49
you just click it and then it just basically expose your API as the MMC server. Now, there's a benefit for that. And the benefit has happened is obviously 0 effort from the customer perspective, right? You click APP and then that basically that make it available. It complete coverage or the endpoint will become available.
576072292608
Jane Star   20:53
Mm.
576072292608
Jacob Phan   21:08
Very easy to experiment today and effectively low government overhead where you how you treated your API, how you govern it today, the same thing that you were doing before now.
On the other side, in practice, things do plan out a bit differently. And this is where if you driven to kind of the harness worlds and the context management world, you see that. So I think to overload, queue accuracy. So because API tend to be for system to use, very granular and very verbose.
So in order to export an API, we tend to expose lots of endpoint and our payload, the output of the endpoint also rather relatively verbose. That file doesn't play that well because of you then have a lots and lots of tool in, if you think about the context window as well, this long, right?
The more we fill the absolute context window, the harder for the models get. Even, I mean, in the in the kind of a YouTube video that I share, effectively what we're saying here is model perform very well if everything you can fit is on the top bit of the context window, it perform worse as you fill to the end of the context window. MCP, because of the way it works, is then...
is then load all the metadata about the tooling, the resources at the point when we run this. And therefore, the more tooling that we have, the more thing we're going to feel on top of this context window, which make our instruction, which is the more the thing that we want it to do, fall into down below. And therefore, what we're seeing is that the performance can be degraded. And it.
It doesn't degrade at the beginning because we don't have the conversation, but as soon as you have loads of these two calling in a conversation, the longer is have the more our thing that we ask within for the for the dial below in the context window, hence why we see that behavior. The endpoint shape is also not the same intention shape. So give you an example, this is actually a real example and this is actually linked to the Google IO.
that we're seeing in the last couple of days is, let's say, a typical commerce experience where add to bag and then cheque out. Add to bag, you want to have a bag API with add to bag API, remove item from the bag, all of these things, right? And then you've got to cheque out our item where, okay, I've done now, let's cheque out this bag and then you go through the payment.
576072292608
Francisco Cachado   23:15
Yeah.
576072292608
Jacob Phan   23:28
So imagine if you going through the shopping and then you say, right, okay, I want to be able to do a shopping journey and cheque out a particular bag. The LLM, if in this very granular, have to orchestrate the add to bag, remove a bag, and so on and so forth. So you have to chain multiple API call.
to accomplish a particular task. So therefore, it's making it harder for it to do. And obviously, if you think about token, the way that we consume it, the more token is then the consumer is you have to call multiple API call, look at it, reason it, we spend our token, and then so on and so forth. So I think what we, what my suggestion is saying is we should treat, yes, if.
We should think about it carefully when we view our MCP server, give it an abstraction layer, or think about it. How would you use, how would you give it to someone to do something, i.e. the intention rather than actual or the API call?
So there you go. That's my simple message. I got a few more slides in terms of maybe what is the best way to go about it. But I think I stop here first, and then just kind of send a message out and say, right, one-to-one relationship is great because it's giving you all of these benefits. But in practice, when you could do it at scale, you're going to see some of these
disadvantage is best to be aware now and don't take it as a clever default approach and then do it and then roll it out. You will then end up with the number of MCP server equivalent to the number of API that you have and the tooling that you have will be the same number of the API endpoint. And then when you then orchestrate all of these together in the agent and the more agent that you work together on the higher level,
the more tooling and the more things that you have to do and therefore you fill out the context window very quickly and then you see that the performance degrade. So I pose here for any questions first.
576072292608
Jane Star   25:24
Yeah, thanks, Jacob Phan. I think we won't do one-to-one mapping for sure, because like building one MCP server just for one tool, that's not mining the full potential of MCP. Like we should always group the tools in based on functionality or the way that was about for use case.
And then have one MMC PM point for a group of tools instead of just one.
576072292608
Jacob Phan   25:46
Yep.
Okay, so think about it. This decision is going to be yours, right? I just share kind of thing. To give you an example of the real life and things how it's going to work. Anyone here using Slack?
Now, Slack instead of T. No, okay, yes, like, yeah, so you know what it's like. So if you look into MCP server definitions of Slack, MCP server versus Slack, its own API, you'll see the massive difference.
576072292608
Jane Star   26:10
Yeah, all of us.
576072292608
Francisco Cachado   26:13
Really? Yeah.
576072292608
Jacob Phan   26:26
So, just give you a point of reference in terms of something that you can see, yeah, and and and that I think that that effectively is is a message that I'm trying to to to send here is if one-to-one relationship would be great for POC and very quick for you to get off the ground, but I think is something that you might want to be aware of the.
576072292608
Sanjay Sardesai   26:27
Absolutely, yeah.
576072292608
Jacob Phan   26:48
some of these shot 4 I highlight on screen.
That's it for me. I think this is for maybe food for thought. Think about it and let me know.
576072292608
Jane Star   26:59
Yup, great.
No.
576072292608
George Smith   27:05
So let me again bring this back to silly pictures so that I can understand.
576072292608
Jane Star   27:09
Mm.
576072292608
George Smith   27:11
This is one option, right, is that we have an MCP server for every single API and we're saying bad idea, your poor old agent has to deal with a ridiculous amount of context because they're going to have 400 MCP servers that they can access. Everything gets complicated, every blah, blah, blah, right? So bad idea. I think then we've got some, we now, I guess we're getting into Jane Star maybe where you wanted to take this.
576072292608
Jane Star   27:17
Please share that, yeah.
No.
Yeah, that.
Mhm.
576072292608
George Smith   27:32
I'm guessing, which is how are we going to do this, right? So are we starting to say that we're going to divide it into system and category, right? So for Maximo, if you're doing anything to do with jobs, we've got an MCP server.
576072292608
Jane Star   27:33
Yep.
576072292608
George Smith   27:43
Or are we going to do something where it's much more general than that, right? If you're talking about jobs, it doesn't matter whether it's Maximo or some other system. If it's about jobs, there's one MMC server for the whole lot.
576072292608
Jane Star   27:46
Yeah.
576072292608
George Smith   27:53
You know, I guess that's the next question, right, is what is a category?
576072292608
Jane Star   27:53
Right, yeah, yeah.
576072292608
Sanjay Sardesai   27:57
And, and you know what, let's say there's one MCP, like, for example, Maximo we are talking about, right? And, like, there are hundreds of agents who want to consume this on the load again, even if we even if we have a underlying AI system to load balance and everything.
576072292608
Jane Star   27:57
Mhm.
576072292608
Sanjay Sardesai   28:17
We are again now dependent on the MCP server for Maximo to work.
properly. So there's one more element which is added into a complexity. Whether if that fails, that becomes a Nick, right? If that fails, all of these 100 agents, whatever they're consuming, they are all.
576072292608
George Smith   28:34
True.
576072292608
Sanjay Sardesai   28:36
Blocked.
576072292608
Jane Star   28:37
So, Sanjay, we're just saying like deploy MCP server in a container is adding more complexity to the picture. Is that what you're saying?
576072292608
Sanjay Sardesai   28:45
Yeah, because AIS or APP is already managing all that heavy loads, load balancing. So APP is more than capable of handling all that plus.
576072292608
George Smith   28:55
So you.
576072292608
Francisco Cachado   28:55
No, but, but, but sorry, on the like, APP is just like a layer that someone requests to go to go there, like, if if we start to like if we containerize the MCPs and deploying, for example, in Akka and the Azure Container Apps, if that if the number of connexions are...
I, it start to spin up more content just to handle all of that communication and then APP, because like APP is just like an abstraction layer.
576072292608
Sanjay Sardesai   29:22
But the question is...
Yeah, yeah, but APP does give you MCP server, like just like Jacob Phan said, right? So all those API endpoints can be easily converted into a MCP server, a group of them, of course, for example.
And we can just use it because it does all the scaling and everything.
576072292608
George Smith   29:44
So, so when we said that you can just turn on an APP API and it and it can be exposed via MCP, is that what you're saying, Sanjay? And can you do that by group so we don't have the problem of one-to-one?
576072292608
Jane Star   29:45
Okay.
576072292608
Sanjay Sardesai   29:45
Right.
Yes.
Yeah, of course. Yeah, yeah.
576072292608
Jane Star   29:56
Are we sure about that? Because I think what Jacob Phan was saying, the current functionality is 1 to one.
576072292608
Francisco Cachado   30:05
Yeah.
Mhm.
576072292608
Pankaj Arora   30:17
That's where toolbox come in, right?
576072292608
Jacob Phan   30:20
Yeah, the I I think the two bot is grouped all various different things together. I think it's just the issue here is if if you can see that my typical example is that is that bad example, right? If you if you want to cheque it out, you just say I want a thing that cheque out, you want you don't want. I mean, if let's say we five, I don't know how many years in.
576072292608
Jane Star   30:20
Well, let's say...
576072292608
Jacob Phan   30:42
in the AI world, let's say two years down the line, typical anthropic, open AI and say, look, we solved the context window problems and we can guarantee context window wherever you, you and your instructions, you can put as much as you want in. There's no, there's no, there's no problem, right?
576072292608
Francisco Cachado   30:49
Yeah.
576072292608
Jane Star   30:58
Mhm.
576072292608
Jacob Phan   31:04
then this problem goes away. The thing is we're seeing is, as a harness, as concerns, if we put more thing into the context window, i.e. because our API tend to be very granular, right, then the more we put in, the more context window we're going to use. And naturally, over time.
The performer will get degraded, because we we we then fill up the context window quite quickly.
576072292608
Jane Star   31:30
I have a question here. So let's say, so there are two ways, I suppose tools. So let's say I want to give this agent 10 tools. So the 1st way is I give it a list of APIs from APP, like no MCP server, it's just like 10 tools.
dump. And then the second one is I put 10 tools behind the MMC server and I give the MMC server to the agent. In my understanding, the 2nd way saves more token than the 1st way because the 1st way you have to like in the context window you have to load.
576072292608
Jacob Phan   31:47
Mhm.
576072292608
Francisco Cachado   31:48
Mhm.
Mhm.
576072292608
Jane Star   32:06
10 API spark in one shot, like there's no dynamic exposure.
576072292608
Sanjay Sardesai   32:09
No.
No.
I don't think so.
But I let Jacob Phan answer.
576072292608
Jacob Phan   32:17
I'm not sure if I get that one right. I didn't get the question right.
576072292608
Sanjay Sardesai   32:20
Yeah, let's.
576072292608
Jane Star   32:21
I thought.
My understanding of MCP is like the protocol is you are asked, the agent will ask, okay, what tools do you have? And then it responds, okay, this is the tools I have. And then I say, Pell give me 2A, then it responds. So it's a dynamic exposure, it's not 10 tools.
576072292608
Jacob Phan   32:25
Yeah.
Yes, is it?
That's right.
576072292608
Jane Star   32:42
directly straight away into context, but the first method is all specs in one go.
576072292608
Jacob Phan   32:45
Jacob Phan.
I think I think on the MCP protocol you got a discoverable endpoint and effectively you basically ask the MCPs to give you the list tool that will be injected into your context window and then the LLM can then choose to invoke that tool or not. That's a separate thing.
576072292608
Francisco Cachado   32:59
Yeah.
576072292608
Jane Star   33:07
Right.
576072292608
Jacob Phan   33:07
But I think it does, and this is why one of the reason why, where you see the adoption of skilled ai agent skill getting more and more popular, and because agent skill effectively do that, where if you look into the skill right, you got the metadata on the top and then the description of the skill on the bottom is when the when would the MCP oh, sorry, hold on.
When the agents or the harness look into the skill, is only load the top bit, it doesn't load the whole things, and that is that is a progress disclosure be the the the the the fund of issue is not about how client load the list of the tool.
576072292608
Jane Star   33:38
Yeah, exactly.
576072292608
Jacob Phan   33:49
It actually, the issue that I highlighted here is under under that surface, where if you expose one-to-one relationship, you get you just got too many tools that expose instead of exposing.
a large number of tool, you expose a more abstract, less number of tool, it will then give you better performance. It's not about how many tool that the LLM get that does that LLM load all the tool at the beginning. They load the metadata of the tool right at the beginning. It's just how many tool you're going to give it.
576072292608
Jane Star   34:04
Mhm.
576072292608
Jacob Phan   34:23
If you give it too many, then you have performance penalty.
576072292608
Pankaj Arora   34:29
Yeah.
576072292608
George Smith   34:29
So, are we saying here?
We, we could give in in our scenario, right, but there's three APIs, right? Add to cart, remove from cart checkout.
We could just give the agent a list of three APIs, right? And it's got to know about all three. So it's, you know, fairly heavy on the context window. It's just got a list of all three. We could expose 3 MCP servers, one for each. I'm guessing that's pretty much the same on the context window, right? It's still got a...
576072292608
Jacob Phan   34:41
Yeah.
576072292608
Francisco Cachado   34:46
Mhm.
576072292608
Jacob Phan   34:49
Mhm.
No, no, I don't think in this scenario, so if you have an MCP server, you would say, let's say you have a commerce MCP server, you've got three to one there, add to cart, remove it to cart, and then cheque out, right? So that if you kind of do one-to-one relationship, what I'm saying here is you still got the MCP server, let's say an e-commerce MCP server.
576072292608
Pankaj Arora   34:56
No.
576072292608
George Smith   35:10
Sure, yeah, so you...
Sure.
576072292608
Jacob Phan   35:16
But instead of having all of these three endpoints, you give, like, say, a checkout endpoint that basically encapsulate all of these three points. So you change the, you change the payload, for example, you change, because if you look into, like, say, I used to work for ASOS, so I know this, like, I know how verbal is our back API is, right?
576072292608
Pankaj Arora   35:35
Oop.
576072292608
Jacob Phan   35:36
For example, if you cheque out a bag, or what did you need? You need the item number and the SKU number, and that was it, right? To construct a bag. If you do, if you look into the actual bag API, and you can see it from, if you open ASOS website and you look at the traffic, you see that the payload is very verbose in terms of how many item has been added, what time has it added, what time has it removed, etc. So all of that kind of metadata.
fill up this context. So the idea here is MCP, you can then scrap all of these data out. So don't include it in your context window. It's not just the input, it's also the output as well.
576072292608
George Smith   36:09
Ohh.
No.
576072292608
Francisco Cachado   36:11
Mhm.
576072292608
Jacob Phan   36:13
Does that make?
576072292608
George Smith   36:13
But that, but that would still work if you had three.
576072292608
John Blog   36:14
So.
576072292608
Jacob Phan   36:16
No, you would have one, you instead of like say, okay, I want the I want the agent to be able to cheque out one bag, so you then construct that that that that tool in MCP to server to say, instead of taking one lease inside say in in the checkout, you you cheque to get the ID of the bag, and then you you have to construct the bag before that.
576072292608
George Smith   36:18
Yeah.
576072292608
Jacob Phan   36:36
And then you got ID at the back. You can change that in the MMC way where you say, right, okay, you want to cheque out the back and he has all the item in the back. So it was one core instead of three.
576072292608
John Blog   36:47
So what were you saying, that big rectangular MCP would be sitting across all these three APIs, okay, removing those, yeah, and there is some, this MCP is a Python code that.
576072292608
Jacob Phan   36:57
Yes, yes, abstract that.
576072292608
John Blog   37:03
has exposes 1 endpoint, which is checkout, and then it works out by itself. It needs to do 20 call or five calls to actually realise the action. Yeah, yeah, it's a bit like how Facebook resolved the problems of too many API calls. They wrapped it into a new protocol in front of.
576072292608
Jane Star   37:06
Yeah.
576072292608
Jacob Phan   37:14
Yeah, that's what I'm saying. Yeah, so that's where...
576072292608
Jane Star   37:19
Yep.
576072292608
Francisco Cachado   37:21
Mhm.
576072292608
John Blog   37:24
of it, right? 20, 10 years ago. Okay, so, and then just to clarify, so...
576072292608
Jacob Phan   37:25
Yeah.
576072292608
Francisco Cachado   37:25
Yeah.
576072292608
Jane Star   37:25
But.
576072292608
Jacob Phan   37:28
Yeah.
576072292608
John Blog   37:32
These APIs.
can be the APIs in Massimo. In fact, I would put these three dots in Massimo if I'm not wrong. You either one-to-one expose them through API management.
Um...
Or this big triangle rectangle, yeah, you created is hosted in container apps, I would think, and he's an MCP server, and he's also exposed to API management. So, so in your API management, you end up with pure APIs exposed as MCP endpoint, or...
576072292608
Jane Star   38:00
Yeah, yeah.
576072292608
Francisco Cachado   38:01
Yeah, yeah.
Yeah, we did.
576072292608
John Blog   38:10
MCP servers, Python written, ACA hosted, also exposed API management.
576072292608
Francisco Cachado   38:17
Yeah, exactly.
576072292608
Jane Star   38:17
Okay.
576072292608
John Blog   38:18
Am I making sense here?
576072292608
Jane Star   38:19
Mhm.
576072292608
Francisco Cachado   38:20
No, no, that's exactly the idea.
576072292608
Jacob Phan   38:20
Right.
576072292608
Francisco Cachado   38:23
is to put all the MCP servers behind the APP and show them as MCP servers inside of APP.
576072292608
Jacob Phan   38:23
Okay.
576072292608
Francisco Cachado   38:31
Yeah.
576072292608
Jacob Phan   38:32
Yeah, so I think what my is drawing is actually encapsulate my message is the MCP server expose via APP or not to the LLM, but is is on an abstract cover abstract where behind that you can have three that three orange dot and orchestrate that.
576072292608
Francisco Cachado   38:41
Yeah.
576072292608
Jane Star   38:49
Yeah.
576072292608
Jacob Phan   38:50
via the MCP server, that give you the better. I think it just at the moment what we are discussing is should the MCP expose 3 dot or one dot, right? So that is my message is do do do one dot because that that can capture intention of the user.
576072292608
Jane Star   38:51
Yeah, just definitely.
576072292608
Francisco Cachado   39:01
Yeah, that that is, yeah.
576072292608
Jane Star   39:05
Yes.
576072292608
John Blog   39:06
Yeah.
576072292608
Jane Star   39:08
Okay, cool. I think we're aligned.
576072292608
John Blog   39:09
Yeah, I would.
576072292608
Francisco Cachado   39:10
Yeah.
576072292608
Pankaj Arora   39:12
A quick question, Jacob Phan.
Do you know the question?
You were saying about the context window and token optimization?
So looking at the documentation and video I saw on AI Foundry Toolbox.
One of the benefits they set of the toolbox is exactly that, that it cleverly manages the token window and the context and only exposes the tool that is required for that user query.
To the agent, apparently there is some intelligence there in the toolbox.
576072292608
Jacob Phan   39:45
Yeah, I mean, what I'm saying does not stop you from using toolbox. Well, because what we're saying here is we're going to be using...
576072292608
Jane Star   39:49
Yeah, you can.
576072292608
Jacob Phan   39:55
MCP as a reusable.
Building block for our agents. So the question is, how, what is the best way to building this MCP server, not about using toolbox or not? You always more than welcome to using toolbox. I think it's just the the point is when we when we asking the question, what is the best way to building the MCP server?
576072292608
Francisco Cachado   39:59
Mhm.
576072292608
Jacob Phan   40:17
There are two schools of thought, right? One to one, or maybe there's abstractions. And I promoting the abstraction for the reason that I highlighted earlier. That was it. This doesn't stop you from using ToolsOrToys.
576072292608
Jane Star   40:23
Mhm.
576072292608
Francisco Cachado   40:25
Yeah.
576072292608
Pankaj Arora   40:25
Correct.
576072292608
Sanjay Sardesai   40:28
But there is also a question which I said that by doing this, we expose every tool via MCP. There is no other option to expose the tool.
Is that what we are agreeing on? That's good.
576072292608
Jacob Phan   40:42
Not necessary. I think the skill, for example, is one thing. So skill is already available and that is something that you can expose. I think MMC will be very common when you want to...
576072292608
Jane Star   40:50
Alright.
576072292608
Jacob Phan   40:53
Um...
Interact with other system.
576072292608
Francisco Cachado   40:59
Mhm.
576072292608
Jacob Phan   40:59
And make that system available for your for multiple agents. That's why that's the benefit of NCP is.
576072292608
Sanjay Sardesai   41:05
Yeah, so for example, there's one endpoint, for example, which does give you some information. So, and it doesn't relate to anything. In that case, how do we do it?
576072292608
Jacob Phan   41:05
Yeah.
Jacob Phan.
Give me an example, like an endpoint, let's say, let's say, let's say an endpoint like get, I'm not sure is Contoso publicly IPO yet, but let's say Microsoft SharePoint, Microsoft share price, right? So that's an endpoint, right? So I have a MCP server for stock, and I would have an endpoint for a tool in to get a particular stock for a particular.
Vendor Microsoft's one of them, then that that will help me how how how would I do it, um, and then...
Depends on what, as a user, what you can have more more tools on on that MMC server, but I think there are also limitation. For example, if you're using VS Code, you know, if you use it, you know there's a limit to 128 tooling registration that we can have.
576072292608
Francisco Cachado   42:07
Mm-hmm.
576072292608
Jacob Phan   42:09
So we don't want to have more than that either. So you want to basically scrub it out. I guess, for example, from a stock API endpoint, you can have.
Search stock, you can get stock by ID. That's another tool. If you know the name of the thing, or you can search by free text, then as a LLM, what you can choose to decide, okay, I don't want to expose the search by ID, right? LLM can, sorry, LLM can search by free text, for example.
Right, so then, instead of exporting 2 API, you like to choose to export one API only, and then save you that context.
576072292608
George Smith   42:48
I thought the whole point of MCP is that when, as you expand the MCP server, right, and you go, we'll add functionality to this MCP server and enable it with another tool, right? So now it can, it doesn't just get stock information, it can also tell you what's in the warehouse of the local shop. You know, there's some new bit gets added and it's discoverable and you're not going to every single agent to tell it.
576072292608
Francisco Cachado   42:56
Yeah.
576072292608
George Smith   43:08
There's now a new tool available. It discovers it, right? It just finds it.
576072292608
Francisco Cachado   43:08
Yeah.
576072292608
Jacob Phan   43:09
No, you are absolute. Yeah, yeah, no, no, you are right there. But what I'm saying here is, the saying is we are versus like one-to-one relationship versus some kind of abstraction, right? I'm saying one-to-one from API, I can have two endpoints doing very similar thing by ID or by free text. Then I can decide it from my MMC server at this point in time to say, right, okay.
576072292608
Francisco Cachado   43:11
Yeah.
576072292608
Jacob Phan   43:31
LLM can work out free text quite quickly. Let's say Microsoft Stock Hot, right? So just export one tool using free text, right? Instead of tool. Now future, you should say, right, okay, I want to have a new future where I buy stock, for example. Yeah, feel free, add them in.
576072292608
George Smith   43:43
Sure.
But it feels like that should not be done at the MCP layer. Like if we can kind of merge APIs together, right, to create a multifunctional API, shouldn't we do that down here and just have the orchestration within the API that is exposed anyway?
576072292608
Jacob Phan   44:01
And.
576072292608
George Smith   44:02
Because then even if you're not AI, you can still use the same, you know, we're building it then lower down the stack, which makes it more reusable.
576072292608
Jacob Phan   44:04
Mm.
576072292608
Sanjay Sardesai   44:08
Yeah.
576072292608
Jacob Phan   44:11
Yeah, that could be an option if you want to reuse it at some point.
576072292608
Sanjay Sardesai   44:11
And.
576072292608
Jane Star   44:12
Mmh.
576072292608
Sanjay Sardesai   44:13
Jacob Phan.
And do you think that then, are we saying that there should not be any tool which can be exposed by any other protocol other than MMC?
576072292608
Jane Star   44:27
I, yeah, that's a direction that I'm pushing for the ToolsOrToys. Do you have any concerns, Sanjay?
576072292608
Sanjay Sardesai   44:32
So...
576072292608
Pankaj Arora   44:34
No, I think it makes sense that we go via NCP for all the tools.
576072292608
Sanjay Sardesai   44:38
I don't feel that. I don't feel that it should be always MCP. But yeah.
576072292608
George Smith   44:44
Why not, Sanjay?
576072292608
Sanjay Sardesai   44:47
Um...
Because there will be scenarios, there will be things, for example, like I said, there will be, if there is any endpoint which doesn't fit into any of the category which we are creating in MMC. How about that then?
576072292608
Jane Star   45:00
Just.
So, Sanjay, we are saying, what about this tool is just like one single standalone tool that we don't want it to group with anything.
576072292608
Sanjay Sardesai   45:07
Yeah, yeah.
Yeah, I mean, we will always have to make sure that it sits into the right MCP bucket so that it makes sense to LLM. And then I'm putting a risk of LLM agent to then find, you know, to navigate it through. So if from my point of view, accuracy of the...
576072292608
Jane Star   45:12
Okay.
576072292608
Sanjay Sardesai   45:30
The agent might go up if I specifically add few tools directly to it.
Um, but then.
576072292608
Jane Star   45:36
But you can you can point the agent to the MMC server, but say you only have this tool.
576072292608
Francisco Cachado   45:46
Mm-hmm.
576072292608
George Smith   45:47
Yeah, just because you've got an MCP server doesn't mean every agent has to look at it, right? So if you've got some really specific thing, then you're only aiming certain agents at it.
576072292608
Francisco Cachado   45:51
Yeah, yeah.
576072292608
George Smith   45:57
And you're right, Sanjay, we might argue that in this case where it's a really specific thing and it's only one API and it'll never grow any further, maybe MCP is not really worth it, but as a principle.
576072292608
Jane Star   45:57
And.
576072292608
George Smith   46:09
There will always be something extra that comes, right? Active Directory, now you'll want to manage a user, then delete a user, then upgrade a user's license. You know, there'll always be, almost always be, extensibility. So why wouldn't we? Unless there's cost or something.
576072292608
Francisco Cachado   46:09
Yeah.
576072292608
Jacob Phan   46:21
Yeah.
No, that there is a very good explanation. I I put it in the chat here, coming from themselves as well, so the so skill versus project from an MMC server, so I just have a look at those, and I think there's a good point that they mentioned here is about when are you using skill, when are you using MCP server, and if you look into when using skill is more like about...
576072292608
Jane Star   46:28
Yes.
576072292608
Jacob Phan   46:42
workflow thing that you can tell the agent to do certain things. So, and then when you look into the MMC section and when to use it, I think one of the point that they're calling out is about when you kind of want to interact with external systems. So I think, have a look at this guide and I think these give you a bit of a, that does have everything. The question I think, Sanjay, was...
576072292608
Francisco Cachado   46:47
Mhm.
576072292608
Jane Star   46:57
Yeah.
576072292608
Pankaj Arora   47:02
I was exactly looking for, I was exactly looking for this. I read this two weeks ago and I was still thinking of finding him.
576072292608
Jacob Phan   47:02
Was asking, does it?
Yeah, yeah.
No, this, this is, yeah, so I think this is more, I think I like this because obviously coming from the author of MMC themselves, they, they, they, they, they relatively unbiased in terms of what is available, so have a look at those. I think they they do tend to use different thing when when
576072292608
Pankaj Arora   47:11
The really good one.
576072292608
Jacob Phan   47:27
Depends on on the use cases.
576072292608
Sanjay Sardesai   47:27
Exactly.
Exactly, that's why, that's why I don't want to blanket it out, because going ahead, going down to three months, we might have something better than MMC.
576072292608
Francisco Cachado   47:30
Yeah.
576072292608
Jacob Phan   47:38
Yeah.
So, MCP was was was quite good, and then this is the kind of what we are what we see in the industry. MCP get the attention of community, explosive adoptions, and then tooling come into play, APP come into play. Everybody says, what is the best way to be a MCP server? So, one-to-one relationship.
576072292608
John Blog   47:40
Jacob Phan.
576072292608
Jane Star   48:00
Yeah.
576072292608
Jacob Phan   48:01
Then that will happen is then contacts window will get fill, performer degraded, and people say, right, okay, what is the alternative? Then skill was born, skill was born, and then we come to that kind of thing. So there we go. So have a think.
576072292608
Jane Star   48:20
Okay, so back to our solution approach, I think we are more or less aligned, to be honest. I think what George Smith has here, enpepsulate most of it, and then we'll add another layer on top, which is toolbox. And for Sanjay, I think for a scenario that you mentioned, like, let's say we really have the case that we only have one tool, we don't really need it.
to be an MCP server, then fine, because Toolbox can also register an open API. It doesn't need to be MCP. So.
Like for the tools, I suggest our solution should be for the tools that we see there's like grouping, categorization, then we put the MCP server in front of multiple tools for the one that you really think is standalone. It's fine, they can stay in APP, open API. And then overall we use Toolbox as a layer on top as a gateway.
to expose to agents so that we have versioning and all that. Does that sound good for everyone? Yeah, okay.
576072292608
Sanjay Sardesai   49:20
Yeah, another another question to have probably is is there any Azure managed service which we can use to just create the MCP servers other than APP because you said APP should that's not a good thing.
576072292608
Jane Star   49:23
Uh-huh.
576072292608
Jacob Phan   49:36
No, no, I'm not saying it. No, no, that's not what I'm saying. I can't say if it was not a good thing. I know. Please don't get that. That's not the message.
576072292608
Jane Star   49:36
Ohh.
576072292608
Sanjay Sardesai   49:44
Burt.
576072292608
George Smith   49:44
Jacob Phan.
576072292608
John Blog   49:44
Right, PM management is just to get away, so, as you've seen in the screenshot of...
576072292608
Jacob Phan   49:47
Oh, okay. Because we're recording, because we're recording, I would like to say out loud, APP is a brilliant tool. I disclaim what Sanjay was saying. I still want to keep my jobs. No, what I'm saying is, no, there is many way for you to implement the MCP server in the Microsoft ecosystem. Obviously, APP work quite well.
576072292608
Sanjay Sardesai   49:47
Yeah.
Jacob Phan.
576072292608
Francisco Cachado   49:55
Jacob Phan.
576072292608
Jane Star   49:55
****.
576072292608
Francisco Cachado   49:57
Yeah.
The.
576072292608
Jacob Phan   50:09
is because it already have the API level interface, the role of registers and everything there. It got the gateway components of that that basically give you easy for you to expose MCP server via that way. You can using function app and we have tooling to building MCP for server on function app as well. So the orchestration or the obsession layer that you put on top
576072292608
Jane Star   50:21
Boo.
576072292608
Jacob Phan   50:32
that could be done by function now. So there's a multiple tool to do so. Choose whatever that you like, really. There's SDK, and I think Fast MCPS server is one of them that was calling out.
576072292608
Sanjay Sardesai   50:38
Yeah.
576072292608
Francisco Cachado   50:43
Yeah, fast, yeah, fast MCP containerized inside of a container environment and others as an existing or hosted MCP server on APP.
576072292608
Jacob Phan   50:47
Yeah.
576072292608
George Smith   50:55
I guess I'm back to why wouldn't we why wouldn't we use APP? If you can tick a box and it does it for you.
576072292608
Jane Star   50:56
All right.
576072292608
George Smith   51:02
And if we're saying that if you want to combine APIs together to make a more single API, that should be done down here anyway, then just create the new API down here, expose it.
576072292608
Jane Star   51:04
Love it.
576072292608
Sanjay Sardesai   51:13
Yeah, absolutely.
576072292608
George Smith   51:14
And turn on.
576072292608
Jacob Phan   51:14
Yeah, that would work, yeah. Then, then you can, you can have you done the API, then because the observation is available, you can one-to-one it, which is fine.
576072292608
Sanjay Sardesai   51:15
Yeah.
Did, did.
But.
The reason I'm pushing it, yeah, the reason, sorry, let me come. The reason I'm pushing it for APP is because the API Centre gives a very good registry of, that's what I've heard. I've not tried it out yet, but API Centre from Microsoft within the APP gives you good registry.
576072292608
George Smith   51:21
And then we don't have loads of servers.
576072292608
Jane Star   51:23
My...
Jacob Phan.
Yep.
576072292608
Jacob Phan   51:38
Yeah.
576072292608
Sanjay Sardesai   51:40
Because if going forward, if you have to do A to A, that's the reason I'm pushing everything needs to be on APP. If we have a tools, agents, and everything, we have registering in APP and then creating an API centre at the registry. So there will be always one registry from Mikey for all the tools, agents, and everything.
576072292608
Jacob Phan   51:41
That's right.
Alright.
Yeah.
Yeah.
576072292608
Sanjay Sardesai   52:01
In one place.
576072292608
Jacob Phan   52:02
Yeah, so also, can I just calling out one thing? So API Centre is actually a separate product.
To APP, you can bring API or MCP or A2A or skill as well, register that to API Center, and that service endpoint A2 endpoint or MCPS server or skill does not have to be within APP. It can be anywhere that you like. So, so for example, if you we have many customer that...
576072292608
Sanjay Sardesai   52:09
Yeah.
Okay.
Okay.
576072292608
Jacob Phan   52:31
multiple hyperscaler. So you got obviously Azure size of thing and then you got ADLS size of thing. But then the question is, well, how do we manage API or even MCP server across multiple hyperscalers? So API centre do that. So you don't have to, you don't have to have things on a PM to be presented on API center.
576072292608
Sanjay Sardesai   52:51
But OK, in the APP gives you the policies, policy, you know, policies and everything, so again.
576072292608
Jacob Phan   52:55
Yeah, yeah, the policy is is is is it is a is a is a different thing, yeah, so so yeah, registry you you you my recommend is you use both you already using APP, so use that, and then you can using API centre for registry repository of source.
576072292608
Sanjay Sardesai   52:59
Good thing, right?
576072292608
Jacob Phan   53:19
Sorry, John Blog, shut up now.
576072292608
John Blog   53:20
Yeah, so I wanted to say that API Centre is, sorry, API Management is an API getaway, right? That's the pattern, okay? So whether we're taking APIs, MCP, A2A, this is the getaway patterns, which is about
You know.
handling concerns around authorizations, implementing policies in front of the endpoints, managing the endpoints, auditing, tracking, blocking, right? So I agree with Sanjay. API management should be in place to front all these MCP endpoints. The other point I wanted to make is
I'm listening into all this debate currently around, you know, this MCP with Anthropic being very much at the forefront of all these thought leadership around this agentic movements. But Anthropic is a generative AI organisations, they create models.
And for them, their approach of workflows, it's pretty much, you know, agent workflows. It's the agent that just take on the asks and just go off and do a lot of things. But I'm over generations where workflows and business processes automations were here way before.
We had agents and the way you orchestrate workflows through codes, you've got long running processes, you've got asynchronous patterns, you've got processes that start and stop and carries, you know, a few days later. So.
So as much as I can see in the industry, the focus is on workflows in models because they are more and more capable. I think we're still in that stage of the industry where this is still looking at workflows for front office. You know, I need to create that financial report for my CFO. So
I'm going to work through, I'm going to go and fetch some data from finance reports. Then I'm going to go and look on the internet at the competitors. And then step three, I'm going to go and collect some data from the fabric or the data bricks. And so it's a workflow in itself, and it's going to start compiling data and then create this nice reports PDF for my finance.
finance officer. But they are those more complex workflow eventually that is going to come along where you're going to need to call involve Massimo, you're going to need to store persist data into a structured format into a SQL database or Databricks or whatever. Then some other process is going to kick off.
And I think you will have this orchestration layer at the top. This is going to become more and more complex. So some of it will have agenthelpdesk, and I think that's where probably you will have the logic apps. I saw in the deck that there is, you've got this, you know, MCP versus logic apps, not MCP, you've got.
Agent framework versus logic apps, but I think logic apps will play this place where you need still this deterministic, and I think you will still, I agree with Pankaj opinion that there will still be some traditional API calls, there will still be some connectors that you're going to want to use.
mixed with those agents that will call MCP endpoints. Yeah, so yeah, that's the point I wanted to make. So I think we should just bear in mind that fine anthropics are very thought leadership in the space of, you know, workflows with agents, but I think, yeah, we still need to think there's still those traditional workflows you'll need to address.
576072292608
Sanjay Sardesai   57:12
Yeah.
576072292608
John Blog   57:13
Does that make sense, or?
576072292608
Francisco Cachado   57:15
Is.
576072292608
Sanjay Sardesai   57:15
Makes sense.
576072292608
George Smith   57:17
It does. So where have we got to, Jane Star? I feel like I feel like I've gone backwards personally. Not backwards in a bad way, but more questions than I thought we had almost. Are you thinking the same or am I over?
576072292608
Jacob Phan   57:18
Yes.
576072292608
Jane Star   57:27
Jacob Phan.
576072292608
Sanjay Sardesai   57:29
You.
Yep.
576072292608
Jane Star   57:31
Well, I still feel we are 90% aligned, like, based on this graph. The rest will probably will iron out more during when we actually build the use case, you know, but I think a general framework from AICOE is like...
build MCP wherever like you have group of tools and there's a need and you can also have standalone tools as API, APP and if you really need it and then we have Foundry toolbox on top. I think this big picture still.
576072292608
Sanjay Sardesai   58:00
Yeah.
576072292608
George Smith   58:02
Yeah.
But that's fine. I think so. I think we're all good with that stuff. I'm still keen that the principle is we use MCP and if we're not using MCP, it's a we agree as it's an exception. Sanjay, right? So in theory, use MCP if there's an example.
576072292608
Jane Star   58:05
Yeah.
Yeah.
576072292608
Francisco Cachado   58:10
Mhm.
576072292608
Jane Star   58:15
Yeah.
576072292608
Francisco Cachado   58:16
Yeah, it needs to be. Yeah, it needs to be because we need to align on like a strategy that everything needs to follow this. And if it's go outside, it needs to have like a very specific reason to don't follow.
576072292608
George Smith   58:19
Yeah.
Yeah.
Exactly. We'll do a KDD and we'll say in this case we're not using MCP because there's no point. Fine.
576072292608
Jane Star   58:28
No.
576072292608
John Blog   58:30
So, but George Smith, when you say not using MMC.
So you are excluding, in this context, you're excluding everything that is non-agentic, basically.
Or you include, yeah, so you're talking just about the use case where as soon as there's an agent involved.
576072292608
George Smith   58:49
Stuff.
576072292608
John Blog   58:50
As soon as there's an agent, that will be MCP involved. OK, yeah.
576072292608
George Smith   58:52
Yes, yeah.
576072292608
Francisco Cachado   58:53
Mhm.
576072292608
John Blog   58:55
Yeah, because I think Foundry still have in the toolbox some connectors of some sort that are not MCP, right? So.
576072292608
George Smith   59:02
Exactly, and we're saying we shouldn't use that.
576072292608
John Blog   59:04
There are fewer and fewer, to be honest, but...
Yeah, okay.
576072292608
George Smith   59:08
Unless, unless there's an exception, right? Unless we agree that we will in this case.
So I think the questions I've got here are the stuff in red, right? So...
576072292608
John Blog   59:13
Yeah, it's like...
576072292608
George Smith   59:17
I think what I'm hearing, Jacob Phan, you're saying is that really, the less APIs you expose, the better to two agents, because that's all complexity, it's all context window, it's all stuff they're going to get wrong eventually. So keep this as efficient as possible.
576072292608
Jacob Phan   59:33
Yep.
576072292608
George Smith   59:34
And if you have to therefore orchestrate in MMC or behind the scenes, do. So we need to think about that as we're exposing APIs through this process, keep it efficient.
576072292608
Jane Star   59:37
Yeah.
576072292608
Jacob Phan   59:46
Yeah.
576072292608
George Smith   59:47
I'm then hearing that we have a choice to make, right? Are we doing the MMC of these APIs that are now made efficient? So the efficient APIs, are we exposing them directly from a PIM through a function app, or are we what I think is the approach you've suggested, Jane Star, which is servers?
576072292608
Francisco Cachado   1:00:05
Yeah.
576072292608
George Smith   1:00:05
That feels like a choice, right? We've got to decide on that and know why we've made that decision.
576072292608
John Blog   1:00:11
When you say server, it container apps, I mean, OK.
576072292608
George Smith   1:00:12
Gould.
Yeah.
Yeah.
576072292608
Jacob Phan   1:00:18
Yep.
576072292608
Jane Star   1:00:19
Okay, we're gonna have someone on the team, too.
576072292608
Jacob Phan   1:00:19
So to be a real a real example of it that you can see within Foundry and very common is MCP for SQL Server.
So we have MCP hosted on anywhere you like, but let's say scenario is container app. We have this SQL database behind the scenes, and then that will then be exposed to the agent. So yes, that's a typical example that you would see.
576072292608
Francisco Cachado   1:00:29
Mhm.
Yeah.
576072292608
Jacob Phan   1:00:45
So, replace that with behind the scene as your backend will be the same thing.
576072292608
Francisco Cachado   1:00:49
Mhm.
576072292608
George Smith   1:00:50
So, it will be saying that the container.
The container solution is the general best practice. I mean, because I kind of heard earlier we were saying if we're exposing an API from APPIM, we should be using APPIM.
Are we saying there's different scenarios, right? Because obviously it's CPI, right? We can't use APPIM to expose CPI. We don't, they're not coming through APPIM. So we can't use APPIM here.
576072292608
Sanjay Sardesai   1:01:05
No, no, so.
So, I think, I think, I think what Jane Star and Francisco is telling is that we need to use a custom fast MCP protocol as a server and host that custom code server on container and expose it and use those as a as a server.
576072292608
John Blog   1:01:12
Think.
576072292608
Jacob Phan   1:01:32
Yeah.
576072292608
Sanjay Sardesai   1:01:33
Whereas my argument was that we already have APIs and functions and ADK and everything which we are already doing it in container, probably not. But I was saying that we don't really need to have another layer of MCP servers, which is custom, rather use it.
576072292608
Francisco Cachado   1:01:34
Yeah.
576072292608
Sanjay Sardesai   1:01:52
Once those API, once those endpoints are exposed to APM, use APMs by default MCP servers to expose it. That was what I was trying to say.
That is something we need to discuss. Yeah.
576072292608
Jacob Phan   1:02:06
Yeah, do apologize. I got to jump out. Any question before I disappear? If not, then I'll follow John Blog and John Blog can steer me if needed.
576072292608
George Smith   1:02:09
Yeah, it works.
576072292608
Sanjay Sardesai   1:02:10
Nice.
576072292608
John Blog   1:02:18
Yeah, I can do too.
576072292608
Jacob Phan   1:02:20
Alright, okay, see you soon.
576072292608
George Smith   1:02:21
Thank you, Jacob Phan. Thank you.
576072292608
Jane Star   1:02:21
No, how good. I think...
576072292608
Francisco Cachado   1:02:22
Yeah.
576072292608
Sanjay Sardesai   1:02:23
Thank you.
576072292608
Jacob Phan   1:02:24
Thank you.
576072292608
Jane Star   1:02:25
So, I will probably just need to look at the APP and see how it it posts MCP. I mean, if it has a well-managed way, but have we looked into APP and see how?
576072292608
Sanjay Sardesai   1:02:38
Now, we can.
576072292608
Francisco Cachado   1:02:39
Mhm.
576072292608
Jane Star   1:02:42
How is it absent? Yeah.
576072292608
Sanjay Sardesai   1:02:43
Yeah.
So, if you want, I can share you a quick, quick view.
576072292608
Francisco Cachado   1:02:47
No, but the thing, the thing is, and this is like more, if you think more like an holistic way on how we're going to proceed further, it's like all the tools that are existing, for example, and we are talking a lot of Barry and the ideas like to start thinking ahead.
of things that are not built yet. So if you think on things that are not built yet and the proposed way to build it, it's more on that view. And then Barry needs to adapt to this view that we are doing now. So what might happen in the future is that a lot of these tools that we have
or Barry will need to be converted to follow under an MMC approach where we group.
576072292608
Jane Star   1:03:32
Yeah.
576072292608
Sanjay Sardesai   1:03:32
I'm not saying I'm not saying we should not use MCP. I'm saying that if we have to, I was just trying to avoid additional custom servers to be developed and maintained. That's what I'm trying to avoid. Okay, can I quickly show my screen?
576072292608
Jane Star   1:03:45
I hear you, Sanjay.
S.
Yeah, yeah, okay.
576072292608
Francisco Cachado   1:03:52
Yeah, Gareth.
576072292608
Sanjay Sardesai   1:03:52
Yeah, yeah.
The end around the...
The.
Tew.
576072292608
Pankaj Arora   1:04:02
Statement.
Yeah.
576072292608
Sanjay Sardesai   1:04:18
So, okay, so let me show you these are the, so these are the, for example, these are the all APIs, right, which are grouped, right? So these dev tools, these are grouped into one. These are multiple APIs. You can call, you can treat them, each of them as a separate tools, yeah. They are under one API. This is what one API look like in APP.
576072292608
Francisco Cachado   1:04:24
Mhm.
576072292608
Sanjay Sardesai   1:04:39
But there are multiple endpoints within that, yeah.
576072292608
Francisco Cachado   1:04:41
Mhm.
576072292608
Sanjay Sardesai   1:04:42
Same here, all the QFM, yeah? All the Foundry endpoints, all the LLMs and everything, these are all nice endpoints which are there, yeah?
576072292608
Francisco Cachado   1:04:52
Yeah, but like to be like...
576072292608
Sanjay Sardesai   1:04:53
Oh yeah, yeah. Now let's say if I have to just expose the dev this dev tools by MCP right now, these these tools which you are seeing here, they already.
They already scalable or whatever, yeah, because they might be probably developed into a faster API servers or containers or function apps or whatever. They already scalable, they already are capable of doing handling everything, right? What I was trying to avoid is that what I'm saying is let's create this MCP servers with an APP because it's all connected, right?
You get an endpoint straight away. You don't have to manage this server at all. Yeah, now you can select expose an API as an MCP server. Yeah, so when I select this, yeah, so I get an option from that APP which set of APIs I want to expose, right? Let's say if I say this.
576072292608
Jane Star   1:05:47
Ohh, I see. Ohh, OK.
576072292608
Sanjay Sardesai   1:05:47
Derek.
Yeah, now I can select all of these right out here, yeah, and then I can say, yeah, then I can select the product and everything, and then when I just create, that's it, my MCP server is created, I get MCP URL, all the connexion policies, everything is connected.
576072292608
Jane Star   1:05:54
Oh, I see. Okay.
576072292608
Francisco Cachado   1:06:08
Yeah, and but for that sort of, like, we are talking about doing the same thing, but we, once you create, there are two options: host, like hosted, and create a new one is to leverage is to leverage APP, but as hosted ones.
576072292608
Sanjay Sardesai   1:06:09
What?
Yeah.
Yeah, so I'm...
576072292608
John Blog   1:06:19
Exactly.
576072292608
Sanjay Sardesai   1:06:20
I am.
No, no, no, that's what I'm trying to avoid, because if you want to expose an existing M.C.P. server, that's again you, you, you, we end up managing that exposed custom M.C.P. server again, right?
576072292608
Jane Star   1:06:35
So, Francisco, I think what Sanjay is telling us is like, APP has its own way to expose.
576072292608
Francisco Cachado   1:06:39
And this.
I know it was like, as I've already.
576072292608
Jane Star   1:06:44
But so what's the downside you see with doing it this way?
576072292608
Sanjay Sardesai   1:06:45
Because.
576072292608
Francisco Cachado   1:06:51
It's like we need to understand if here we can divide the things and there is like and there is always this problem.
scalability and moving from environment to an environment. If we move this to the next environment, all of this needs to be done through almost click ups, like all of these tasks needs to be always done in the UI every time we need to create a new environment. We need to get like a very detailed runbook on how to do this.
576072292608
Jane Star   1:07:13
Right.
576072292608
Sanjay Sardesai   1:07:13
No.
APP.
But, but I trust you, Francis, you will find out the way to do it, therefore.
576072292608
Francisco Cachado   1:07:19
Um...
576072292608
Jane Star   1:07:22
Jacob Phan.
Yeah, like if you can click on Azure, there must be some script you can write too.
576072292608
Sanjay Sardesai   1:07:25
Yeah.
576072292608
Francisco Cachado   1:07:25
Jacob Phan.
576072292608
Sanjay Sardesai   1:07:27
Gareth.
576072292608
Francisco Cachado   1:07:27
Is he?
576072292608
Sanjay Sardesai   1:07:29
Yeah.
576072292608
Jane Star   1:07:32
All right, but let's say if we can code this, if we can code and then like use the APP and way to set up MCP server, I don't see a big downside in this, Francisco, what do you think?
576072292608
Francisco Cachado   1:07:33
That's it.
576072292608
George Smith   1:07:40
It.
The downside of this is when we're not using APPIM.
576072292608
Francisco Cachado   1:07:47
Mmh.
576072292608
Jane Star   1:07:47
A sort of saying we're not going to use.
576072292608
Sanjay Sardesai   1:07:49
No, my all the APP needs to go via APP, right?
576072292608
George Smith   1:07:53
No success factors, they're exposed via CPI.
576072292608
Sanjay Sardesai   1:07:57
We might then have to register them into APP.
576072292608
George Smith   1:08:00
Well, we could do, right? That is an option, but we're doubling up on middleware, you know, I'm just saying that that is a downside of this.
576072292608
Sanjay Sardesai   1:08:03
Tew.
Yeah, but I think...
576072292608
Francisco Cachado   1:08:08
Yeah, because we are looking, we are looking too much into the like EFF domain, but if we start to think on like the other tools, we might have to do like very custom.
576072292608
Jane Star   1:08:09
I think...
576072292608
Sanjay Sardesai   1:08:18
Yeah, but we can.
So, APP can also do a bypass here, so the reason I'm pushing for APP is that everything stays in one place, all the APIs, because there's that's a standard tool which we have been always using within Contoso, right? The APP is our standard API gateway, so that's the reason I was pushing.
576072292608
George Smith   1:08:28
Correct.
Yeah.
576072292608
Francisco Cachado   1:08:34
Mhm.
576072292608
George Smith   1:08:35
It does really help if we bring everything.
576072292608
Francisco Cachado   1:08:36
Yeah, but on that I fully agree, but on that I fully agree that we should have a centralised place where we registered the entire thing that we are pulled on the same page.
576072292608
Sanjay Sardesai   1:08:42
Yeah.
576072292608
Jane Star   1:08:45
Okay.
576072292608
Francisco Cachado   1:08:55
Mmh.
576072292608
John Blog   1:08:55
what traffic, what goes in, what goes out, for charge back, you know, say you want to, not saying you do, but even show back, you know, who's using the Massimo MCPs and this type of thing. So it allows you to do quite a bit of management there, yeah.
576072292608
Francisco Cachado   1:08:58
Yeah.
Yeah.
576072292608
John Blog   1:09:16
But it's also for the model, so yeah.
576072292608
Francisco Cachado   1:09:16
I think, I think, yeah, I think you know the more the conversation is around on how we are deploying and how we are creating all of these. I think the conversation is more also regarding fast APP like the function apps or server, server less versus server option, and yeah, the same thing.
Sufferless MCP or server MCP. I think the question is a lot about these two approaches.
576072292608
George Smith   1:09:45
Yeah.
576072292608
John Blog   1:09:47
But you would still, okay, but you could decide that every MMC server we create, we're just going to go Pythons on container apps, right?
It's just a decision you have to make.
576072292608
George Smith   1:10:00
Well, I think that's where we are now, John Blog. I think that's where the guys are.
576072292608
Jane Star   1:10:00
Jacob Phan.
576072292608
John Blog   1:10:02
And then you decide to, yeah, okay.
576072292608
George Smith   1:10:05
But the question is, is that the right thing to do? If we then have, in three years time, we've got 400 Python custom code server apps running that we then have to support, is that going to be better than us having created them all through APPIM?
576072292608
Jane Star   1:10:17
Mhm.
Yeah.
576072292608
George Smith   1:10:21
And I would suspect the answer is no, but...
576072292608
Francisco Cachado   1:10:21
Mhm.
576072292608
John Blog   1:10:24
Yeah, but okay, through a Team, you will just create those.
576072292608
Francisco Cachado   1:10:24
Mission.
576072292608
John Blog   1:10:29
expose the existing APIs. But you see the other one is expose an existing MMC server. So API management is just acting as a gateway. It's not actually the MMC server itself, right?
576072292608
George Smith   1:10:31
Yeah.
576072292608
Francisco Cachado   1:10:36
Mhm.
Yeah.
576072292608
George Smith   1:10:41
Correct, but we're saying we wouldn't ever do that.
576072292608
Francisco Cachado   1:10:42
Mayes.
576072292608
John Blog   1:10:43
Yeah.
576072292608
Francisco Cachado   1:10:45
Yeah, I think you, you.
576072292608
Sanjay Sardesai   1:10:45
We're trying to avoid that, yeah, yeah, so this is all the this pushes all just because after that we know we have to manage this all, and I'm just trying to reduce that effort.
576072292608
John Blog   1:10:57
Yeah.
576072292608
Francisco Cachado   1:10:57
Yeah, no, no, like I think I think that the question here on the MCP side on the part of the server is it's around if we if we if we go to a route of a serverless approach or a server approach. I think it's always around that around that topic.
576072292608
George Smith   1:11:16
So how do we get to a decision on it?
576072292608
Sanjay Sardesai   1:11:20
Microsoft Support Foundry Platform and MCP Server Meeting 2.
576072292608
George Smith   1:11:24
Well, that's what I don't want to do is just, I mean, I know you're joking, but we, you know, we want to not cycle through this. So I guess we need, I don't know whether it needs, whether we can, Jane Star, write it up and say we plan, you know, maybe Francisco, you need to cheque whether we can do the Terraform scripts to do that. If that maybe that's the main remaining question, right? Can we code it up?
576072292608
Jane Star   1:11:27
I don't know.
576072292608
Sanjay Sardesai   1:11:27
Jacob Phan.
576072292608
Francisco Cachado   1:11:28
Yeah.
576072292608
Jane Star   1:11:38
Yeah.
576072292608
Francisco Cachado   1:11:42
Yeah.
Yeah.
576072292608
John Blog   1:11:44
I mean, all the APP.
576072292608
George Smith   1:11:44
And if we can, we say, right, APP is the answer. Here's why.
576072292608
John Blog   1:11:47
APP, all the APP stuff, you know, has got GitOps models behind it, so it can all be automated, right? Deployment of the API management itself, but also of the APIs with the policies. So, it's all through code, so that the operation team is going to be managing all the bicep, all the Terraform you said for
the Foundry, the, you know, et cetera. They will also have a repo for the APP management and the, you know, you can even automate someone else. We flag the new MCP server and it's just get added to, you know, a list and then an agent in the background just, you know, kicks in and then that's where the GitHub co-pilot.
576072292608
Jane Star   1:12:12
Online.
576072292608
John Blog   1:12:28
kicks in in the background and it's just create a deployment for you. It's one click, you know, and the MMC server is there. I think you should leverage as much as possible the GitHub Copilot in the back end, you know. Sanjay is going to smile and say, hey, he comes again with GitHub Copilot, but because that is going to take care of a lot of the automations for you on the back end.
576072292608
Jane Star   1:12:30
Okay.
576072292608
George Smith   1:12:46
Yeah.
576072292608
John Blog   1:12:49
Right.
576072292608
Francisco Cachado   1:12:51
But it's sorry, sorry, I'm quite a bit lost now. Vitam Copilot, when in which place?
576072292608
John Blog   1:12:58
Sorry, yeah, just so I'm saying is everything you're talking about you want to build here, you're going to have to write scripts for it. Okay, so yeah, so you're going to have a repo with Terraform scripts, okay?
576072292608
Jane Star   1:13:06
Yeah.
576072292608
Francisco Cachado   1:13:07
Yeah, forum screws.
Mhm.
576072292608
John Blog   1:13:14
So GitHub Copilot can help you build those scripts, okay? So, and can help you build the pipelines and can help you understand how you do the automation.
576072292608
Francisco Cachado   1:13:20
Yeah.
576072292608
John Blog   1:13:25
But you can also have agents that will, maybe that's for another conversation, but that will come and explore how your system is behaving and what is being noticed in terms of some of the patterns and then do some recommendations. So I might be stepping into a completely different domain here, but
576072292608
Francisco Cachado   1:13:42
Okay.
Tew.
576072292608
John Blog   1:13:47
The concerns of having too much to manage can be compensated by some more AI these days.
576072292608
Francisco Cachado   1:13:47
Okay.
576072292608
Jane Star   1:13:56
Okay, so I think three things as next step for all of us to think through and then we can in the next meeting we make a decision on this. So first it was like whether we all agree like we want APP to be this centralised place where like all the endpoints go in. Second is for the MCP server like how and where we deploy it.
576072292608
Francisco Cachado   1:13:56
Singh.
576072292608
Sanjay Sardesai   1:14:05
Yeah.
Yes.
576072292608
Jane Star   1:14:17
Is it in APP? Is it a container? Like, what's the pros and cons for all of them? And then the third one is like, just cheque whether we can do write code to deploy the MCP server in APP. Okay, all right, let's all sit on.
576072292608
Francisco Cachado   1:14:31
Yeah, yeah, we just need to that assessment.
576072292608
Jane Star   1:14:35
Cool, cool. Yeah, let's do our investigation and we think through and then we regroup next week. All right, but I think oh yeah.
576072292608
Francisco Cachado   1:14:36
Mm.
576072292608
George Smith   1:14:42
So we got the standing meeting on Tuesday. So yeah, if we can try and Jane Star write this up or whatever and try to isolate any remaining questions we have, then in the big meeting on Tuesday, we can review it and then agree next steps if we need any more.
576072292608
Francisco Cachado   1:14:42
Yeah.
576072292608
John Blog   1:14:44
Yeah.
576072292608
Jane Star   1:14:45
Yep.
Yeah, I will.
576072292608
Francisco Cachado   1:14:47
Yeah, right.
Yeah, exactly.
576072292608
Jane Star   1:14:53
Right.
576072292608
Francisco Cachado   1:14:53
Yeah, exactly.
576072292608
John Blog   1:14:53
So that one will need to be postponed, I'm afraid.
576072292608
Jane Star   1:14:54
Jacob Phan.
576072292608
George Smith   1:14:59
Ohh.
576072292608
John Blog   1:14:59
Because.
576072292608
Jane Star   1:15:00
Otters.
576072292608
John Blog   1:15:02
Well, we would like...
I think you know, George Smith, would like Paul now to be...
576072292608
Jane Star   1:15:06
Jacob Phan.
576072292608
John Blog   1:15:10
present on all these calls on Tuesday afternoon. But this time of the week doesn't work for her. So going forward, maybe not the next one, but the one after will need to be rescheduled so it works for her.
576072292608
George Smith   1:15:14
Mhm.
Okay.
Let's talk about that then on the next on the next Tuesday meeting. Let's talk about when we can reschedule it to with everyone there, hopefully. I mean, obviously, maybe Corner won't be, but...
576072292608
John Blog   1:15:37
Okay. Okay. I had prep to talk about, we're not going to do this now, but about the way the foundry, one foundry, one foundry per domain, departments. Is that next on the agenda for Tuesday or?
576072292608
George Smith   1:15:38
Let's try and talk about that next time.
Yes.
576072292608
Sanjay Sardesai   1:15:51
Yes.
576072292608
John Blog   1:15:52
or we want to close the MMC first, maybe.
576072292608
Sanjay Sardesai   1:15:55
I've got that.
576072292608
George Smith   1:15:58
Can we talk about that briefly now, or do people need to?
576072292608
Sanjay Sardesai   1:15:58
designers.
576072292608
John Blog   1:15:58
We, we can maybe close.
576072292608
George Smith   1:16:02
Jump off.
576072292608
Sanjay Sardesai   1:16:03
This is a very high level, just food for thought. I'll just give this. This is what I've been doing at the moment as we set up the EL landing zone. So we have got non-prod subscriptions and prod subscription within non-prod. We are using dev, segregating the dev with resource group and dev with, sorry, test.
Resource group for each domain, then we have production, that's it.
576072292608
John Blog   1:16:28
Yeah, OK.
576072292608
George Smith   1:16:29
But you're doing those domains by business function, right? So you've got like, basically you've got engineering and you've got HR so far.
576072292608
Sanjay Sardesai   1:16:33
Yeah.
Yeah, so this is a, yeah, yeah, yeah, so at the moment this is just true, yeah, but we we will.
576072292608
John Blog   1:16:40
OK, so it's one, and then one project per use case in each Foundry instance.
576072292608
Sanjay Sardesai   1:16:46
So in Foundry instance, there might be multiple projects, but at the moment there's only one, yeah.
576072292608
John Blog   1:16:50
Yeah.
Okay, so yeah, that's what I was going to, that's, it's interesting. This is how I was, we were, Jacob Phan and I were going to suggest the approach, right? So one RG per domain and with one instance, but one project per use case, yeah. Okay.
576072292608
Sanjay Sardesai   1:17:09
Yeah, yeah.
576072292608
George Smith   1:17:10
But I just, can I just make sure though that we can share those resources, right? The HR, if the HR instance subscription, whatever it was, you can remove the diagram so I'm lost. You know, if that has an agent in it that does something that is multifunctional and would be useful to have in the engineering space or to be consumed by.
576072292608
Sanjay Sardesai   1:17:11
So we are in India.
576072292608
George Smith   1:17:29
something in the engineering space. Can they talk to each other? Can we cross boundaries or are we locking ourselves out?
576072292608
Francisco Cachado   1:17:30
Mm-hmm.
576072292608
Sanjay Sardesai   1:17:34
They should, if they should, I think, yeah, because if you're doing a common ai registry, that they should.
576072292608
Francisco Cachado   1:17:43
Yeah, true, yeah.
576072292608
John Blog   1:17:43
Yeah, that's where your orchestration layer would call upon this different agent in this different domain. Yeah. But at least you've got a way to gate who has access to this different domain. Yeah.
576072292608
George Smith   1:17:48
Okay.
Jacob Phan.
OK.
576072292608
John Blog   1:17:57
But then there was the point about there's a pattern around, I can see the API management. It's a big question, but the one of the pattern is it's to expose models as well. So in addition to these Foundry instances, you've got a hub Foundry instance that has the models.
And the models are exposed through API management. So each of these AI Foundry instances don't actually use, don't actually deploy models. All they have is agent observability tools, but they consume agent from a centralised Foundry instance.
because that allows you to share models, that allows you to control who has access to models, allows you to manage life cycle of models, you know, model that get retired. Think about like how many models you, I mean, instance, you're going to have each of one with a lot of different models or when 4.1 is retired, how are you going to know?
which instances uses 4.1, and you know, think about retiring these models if you have one centralised way of deploying models. So this is one of the patterns is to have centralised deployment of models.
576072292608
Francisco Cachado   1:19:18
Yeah, he had like a, he had like an open spoke topology would be better than like the app being like a centralised place and all the spokes would be each specific domain.
576072292608
John Blog   1:19:19
So, Rob, I don't know if this, yeah.
Yeah, if I can just share my screen.
This is the slide I had prepared.
Yeah, so basically, same as you were showing, Sanjay, but instead of each one having their models, you've got this hub RG that's got its own foundry. Maybe there's going to be some shared agent potentially, but most importantly, there's going to be models that are deployed.
576072292608
George Smith   1:19:46
Awan.
576072292608
Francisco Cachado   1:19:47
Yeah.
You don't have it.
Mhm.
576072292608
John Blog   1:20:04
Um...
Through the IPPI gateway, so we talked about the MCP, the Massimo APIs, the A2A, they all get.
576072292608
Francisco Cachado   1:20:16
Mhm.
576072292608
John Blog   1:20:16
catalogued and registered here. And that's where you've got all the different patterns for the EI gateway. You can put some auditing, you can put some load balancing. And it could be you're going to have a model that really needs to consume a lot of tokens. So you might decide that one specific workload is going to have its own model deployment.
576072292608
Sanjay Sardesai   1:20:23
Simply, yeah.
576072292608
Francisco Cachado   1:20:26
Mm-hmm.
576072292608
John Blog   1:20:38
And, but at least when, yeah, when you got got the times of model retirements, you know exactly through the auditing who is using 4.1. You can also block, you can put some some fresh, you know, some what's the word I'm looking for?
576072292608
Francisco Cachado   1:20:38
Mhm.
576072292608
John Blog   1:20:58
Um, some throttling and yeah, capping, yeah.
576072292608
Francisco Cachado   1:20:58
Some capping, capping in.
So you control, yeah.
576072292608
Sanjay Sardesai   1:21:05
Yeah, all of that we can do it in the policies right there.
576072292608
Francisco Cachado   1:21:06
It is.
Yeah, so, so that's like that's that's that's the diagram. It's still to be refined to once we start also having like the development on other domains to have like a consensus and like a better standardised approach for all the for everything.
576072292608
John Blog   1:21:09
Correct, yeah.
576072292608
Sanjay Sardesai   1:21:20
Yeah.
576072292608
John Blog   1:21:28
Okay, so you've got the doc for the AI getaway with API management.
576072292608
Sanjay Sardesai   1:21:28
Cook.
576072292608
John Blog   1:21:34
You've got the article.
Do you have the article or do you want me to share it again?
576072292608
Sanjay Sardesai   1:21:39
No, yeah, you can share.
576072292608
Francisco Cachado   1:21:39
Yeah.
Yeah, if you can share it, it would be good.
576072292608
John Blog   1:22:09
The link, OK.
576072292608
Francisco Cachado   1:22:09
Yeah.
576072292608
John Blog   1:22:13
Um...
Of.
That's probably enough to go through for Friday afternoon.
576072292608
Jane Star   1:22:21
Jacob Phan.
Yeah.
576072292608
Francisco Cachado   1:22:23
Yeah.
576072292608
George Smith   1:22:24
Yeah, thank you, John Blog. Sorry, I realise we've overrun them massively. So thank you for your help and thanks everyone else.
576072292608
Jane Star   1:22:24
Yeah, thank you so much. Yeah.
576072292608
Sanjay Sardesai   1:22:26
Thank you.
576072292608
John Blog   1:22:27
No, no, that's fine, that's fine. I can spare more time, but I realise this is...
576072292608
Sanjay Sardesai   1:22:28
Yeah.
576072292608
John Blog   1:22:33
Yeah, there's another one here.
We know the, I know very well the guy who's written all this, so...
Can bring him in if needed.
576072292608
Francisco Cachado   1:22:44
Okay, perfect.
576072292608
Sanjay Sardesai   1:22:45
OK.
576072292608
John Blog   1:22:46
Thank you.
576072292608
Francisco Cachado   1:22:47
Thank you very much.
576072292608
Sanjay Sardesai   1:22:47
I think, yeah. Well, thank you all. Cheers. Bye, bye, bye.
576072292608
George Smith   1:22:47
All right. Thanks very much, everyone. Have a good long weekend.
576072292608
Jane Star   1:22:48
Okay.
576072292608
Francisco Cachado   1:22:49
Smith.
576072292608
John Blog   1:22:50
Have a good weekend. Bye-bye.
576072292608
Francisco Cachado   1:22:51
Good weekends.
576072292608
George Smith   1:22:51
See you later.
621792274320
George Smith stopped transcription

