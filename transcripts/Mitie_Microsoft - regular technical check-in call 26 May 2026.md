# Mitie_Microsoft - regular technical check-in call 26 May 2026

_Extracted from Mitie_Microsoft - regular technical check-in call 26 May 2026.docx_

---

MitieMicrosoft - regular technical check-in call-20260526_130032UTC-Meeting Recording
26 May 2026, 01:00pm
1h 15m 57s
576072292608
Sourabh Sardesai   1:15
Hello.
576072292608
Helen Foy   1:17
Hi.
Just gonna hammer.
I'm just in. Hi.
576072292608
Francisco Cachado   1:26
Hello, Aviva.
576072292608
Helen Foy   1:28
I'm in the middle of switching laptops at the moment, so all my settings are a bit wonky. I'm on my laptop camera. Normally I use one that's attached to my monitor, so I'm at a bit of an odd angle as well.
576072292608
Mike Agar   1:43
So, no worries.
576072292608
Helen Foy   1:44
Mm-mm.
576072292608
Mike Agar   1:53
We'll just give it a minute.
576072292608
Francisco Cachado   1:56
Yeah, Emma just sent me a message telling me that she will be a little bit late to discuss, so once you have everyone, Mike, I think we can stop this.
576072292608
Mike Agar   2:11
Ed.
576072292608
Sourabh Sardesai   2:16
Give me a minute.
576072292608
Mike Agar   2:21
Who else are we missing?
Are we getting anyone else from Microsoft today? Do you guys do you guys know Ha or Isabelle or anyone else?
576072292608
Helen Foy   2:38
As I'm aware, people are coming. I don't know if you know differently than Vincent.
576072292608
Vincent Rouet   2:43
No, so I thought Ha would be, we know Paul now is not available, but I thought Ha would be joining.
I didn't confirm.
576072292608
Helen Foy   2:55
Do I ping? Let me do some painting.
576072292608
Mike Agar   3:00
So let me get started. In the meantime, I guess we can at least discuss kind of where we've got to. So obviously, last week, we identified a couple of big areas that we wanted to talk about more. I should say, I guess we presented the sort of initial view of the overall kind of golden platform. I think in general,
People were broadly happy with that, though there was lots of kind of deep dive elements in areas. As I say, the key two areas that we wanted to talk about there immediately, I think, were around Foundry, the domains within Foundry, and also MCP, you know, how should we be using
MCP. So we had a meeting about that on Friday. I have sent meeting minutes out off the back of that meeting, so I'm happy if we want to just whiz through that and make sure I've captured everyone's thoughts okay. So maybe that's one agenda item.
576072292608
Vincent Rouet   3:40
Mhm.
576072292608
Mike Agar   3:56
The other agenda item is anything else we want to continue to discuss and I'm aware we're very sort of week by week at the moment and we're sort of trying to book meetings in for the week that we're discussing them in. So I'd like to try to get a bit ahead of that if we can and book things a little bit more in advance. But for now, what is the next thing that we need to discuss?
and talk about, so Emma, Francisco, I guess I'm looking at you guys just to kind of work out what we need to do this week.
576072292608
Sourabh Sardesai   4:20
Thanks.
576072292608
Emma Sun   4:20
Jay.
Yeah, of course.
576072292608
Sourabh Sardesai   4:21
I think, for the sorry, I'll just take one. So, we, I think we need to 1st have a discussion on MCP internally, and then we can move back to, we can discuss it again with them. I don't want to need to just have a catch up to that.
576072292608
Mike Agar   4:36
Okay.
576072292608
Emma Sun   4:37
Right, totally agree with Sourabh. Let's close out the tool build decision first, which is related to MCP. And then we can talk about the domain segregation. I think we still have a little bit left there. Yeah, I think that's probably the meeting today.
Ohh, just to ohh, yes, Ha.
576072292608
Ha Duong   5:01
Oh, no, no, no. I raised my hand. So you can please finish. I raised my hand so then I can be out there. Don't worry.
576072292608
Emma Sun   5:09
Oh, okay. So just recap for everyone, like from Friday, right? And also Mike also wrote a good meeting minutes. So basically, I think we were thinking about whether we should use APP as a centralised place for all the APIs.
And like basically, all our tools will be APIs. And I think we want to use APP and then use the native functionality in APP to convert to MCP server.
So, for this decision, like, does that sound good and as a best practise for the Microsoft team to keep us interested? Yeah.
576072292608
Sourabh Sardesai   6:00
And Ha and Ha recommended that APP is really good tool.
576072292608
Emma Sun   6:05
Yes.
I think one thing that we...
Aren't 100% sure is like we we see the on the UI version how we can change APP into an MCP server. Does it have a pro code solution for us to do that?
576072292608
Vincent Rouet   6:26
Yes, I have. I've prepared a demo for you on this. Yeah, I spend the day scripting and read GitHub Copilot, so got something working I can share on a repo.
576072292608
Emma Sun   6:26
Your gas now?
Oh, amazing. Yes.
Yeah, nice. So basically, Vincent, that's a cold version.
576072292608
Mike Agar   6:40
Well.
576072292608
Francisco Cachado   6:42
Ed.
576072292608
Vincent Rouet   6:44
Mhm.
576072292608
Francisco Cachado   6:44
Yeah, but Vincent, the demo that you prepared in terms of code, what is the code that is being used to create those MTPs inside of APP?
576072292608
Vincent Rouet   7:00
some Terraform, and then in some Terraforms that don't have the resources, it's going to use some of the APIs or some, yeah.
576072292608
Francisco Cachado   7:02
OK, thanks. OK, but that's exactly.
Yeah, the API, yeah, the Azure APP, okay.
576072292608
Emma Sun   7:13
Okay.
576072292608
Vincent Rouet   7:13
Yeah, because Terraform is always behind the Microsoft native resources, so yeah.
576072292608
Francisco Cachado   7:17
Bing.
576072292608
Mike Agar   7:22
Great, so we can maybe cover that in the call if we can.
Um...
576072292608
Emma Sun   7:28
Mm.
576072292608
Ha Duong   7:28
Yes.
576072292608
Emma Sun   7:29
Yes, I mean, if Vincent, do you have code ready for us to see together? Feel free to share your screen. Or else, like, since you already confirmed with us that this can be done through Terraform, I think that's a good enough answer. Like, we can, we would just want to confirm that there is a code solution, because if there's only...
576072292608
Ha Duong   7:43
Yeah.
576072292608
Vincent Rouet   7:50
Yeah, we can do, yeah.
576072292608
Emma Sun   7:52
Yeah, okay, awesome. I think...
576072292608
Vincent Rouet   7:54
We can do an offline session if you want just on that, but it's just to say that we've got something working.
576072292608
Emma Sun   7:57
That's fun.
Yeah, yeah, I think that that's fine. As long as you guys confirm that there is a protocol solution, I think we are we are good. So, to the mighty team, I think for this MCP server, we we should go with this one, right? APP and MCP server.
576072292608
Mike Agar   8:15
So, what?
So I think that makes sense. What we do need is we need to get back to the KDD documents we said we'd write. So I think we just need a quick KDD that says we will use a PIM, here's why, here's why we're not using servers, just to make sure we're all, we've got the backing behind it. The other thing is you said earlier, Emma, that
576072292608
Emma Sun   8:19
Mhm.
Thanks.
576072292608
Ha Duong   8:29
Ha.
576072292608
Emma Sun   8:33
No.
576072292608
Mike Agar   8:36
ToolsOrToys would only be APIs.
I don't think that's true, is it? It couldn't at all be.
576072292608
Emma Sun   8:41
Yeah.
Thus.
576072292608
Mike Agar   8:44
a function APP or something else.
576072292608
Sourabh Sardesai   8:47
So, even even if it is function up, Mike, it's still going to have an endpoint; it still needs to be.
576072292608
Francisco Cachado   8:52
Yeah, yeah, exactly. I think Sourabh, I was muted. I was saying exactly the same thing, so, like, even if it's a function app, it's expose an endpoint, so that endpoint, since we are we are using APP, then it's just like a matter of just collapsing all of that in grouping them in a in an MMC server inside of APP.
576072292608
Mike Agar   8:54
Okay.
Okay.
576072292608
Emma Sun   9:09
Mm.
576072292608
Mike Agar   9:14
And there's nothing else that we would be exposing. We, I mean, we talked about things going out via CPI, right? And we're saying we would wrap that through AIS even then.
576072292608
Ha Duong   9:21
Yeah.
576072292608
Sourabh Sardesai   9:23
Yeah.
576072292608
Mike Agar   9:23
so that it can be exposed via APP as an MMC.
576072292608
Sourabh Sardesai   9:25
Yeah, if, if, if they have, yeah, if, if you want to use IFF in somewhere, then we do that understand it.
576072292608
Mike Agar   9:35
Okay, so yeah, so I definitely think we need that KDD to come together and we can cross that one off. But I think it sounds good. Sounds good.
576072292608
Emma Sun   9:40
Yeah.
576072292608
Francisco Cachado   9:42
Mmh.
576072292608
Emma Sun   9:42
Nice. So Mike, I will definitely document this in SDD, but do we also need a KDD on this because this is continue is a continuation from how the team is building to today. So it's not different.
576072292608
Mike Agar   9:58
I think we need to start, because I've just been having conversations with other people about our auditability and our control of decisions. And I'm sort of saying, oh, we've got this huge platform document coming soon. And I think there's a lot of decisions we're making as we go. And I think we need to start pulling them out. We can use AI, Emma, right? So it's not like we have to write it twice.
But yes, I think we need to start getting some of these things out into KDDs. I'm happy to help. So that we can start to sort of say, this bit is done, this bit is done, this bit is done. Otherwise, we're going to wait.
576072292608
Emma Sun   10:23
Oh, sure. Yeah, yeah. Oh.
Okay.
576072292608
Mike Agar   10:31
What could be a fair amount of time, Emma, and we'll never quite know where we are with the whole document. So yeah, I think we need to start getting some KDDs sorted.
576072292608
Emma Sun   10:40
Okay, Mike, do you mind owning that piece? Because I'm focusing on the SDD. It will be very helpful if you're owning that and then just like tracking all these decisions. We can discuss more offline, but yeah, okay. Thanks so much.
576072292608
Chris Snowden   10:49
Yes.
576072292608
Mike Agar   10:51
Yeah, yeah, we can discuss it.
576072292608
Chris Snowden   10:52
It's not, it's not, it's not really from IT though to populate it. That's the only thing I would say. I'd be looking at you guys to be populating the KDDs and then we can obviously take it through getting approvals and things like that in whatever forum it is, but
576072292608
Emma Sun   11:05
Mm.
Okay, sure, Chris. Yeah, yeah, I will talk more about this with Mike offline. Amazing, but overall I think we are all aligned about tool build, right?
Call.
576072292608
Ha Duong   11:20
Can I just jump in on this one just very quickly? I think as part of the credit, I think we need to prove why we're doing it and do it any quantitative that we measure. So as part of that, and I think we talked about Maximo quite a bit in
576072292608
Emma Sun   11:23
Ha.
576072292608
Ha Duong   11:38
in our conversation. So what I did was let me share my screen.
No, no.
And the weather is so hot. My machine is very slow.
576072292608
Mike Agar   11:50
She.
576072292608
Chris Snowden   11:50
Yes.
576072292608
Ha Duong   11:52
So I need a new machine.
I shared a screen on maybe this way is maybe a bit easier. This is a public repo that I built. You can have a look at those. I share that in the chat. But I think what I wanted, I think one of the conversation we had last time was what is the value? Why are we doing?
Why do I suggesting not a one-to-one relationship? What is the value we're going to get out of it? Okay, so I said, okay, right, let's just see. So I researched it into kind of the Maximo API, and I presume this is mine. I'm getting the right ones. If you have a native relationship, effectively, we can do this proposal.
Alternatively, we collapse this into these architecture here. So you've got MCP client, it could be anything, right? It could be your agents, could be co-pilot, etc. APP will then funding that, offering all of these capability, validate Jake token, rent limiting.
Cause, etc. We got the I have here is a mock server for Maxima. So this is not Maxima, but it is a mock of it based on the API that I researched about. And then the abstractions, which I think we talked about last week, were this one. Now, because we suggesting using Container App.
in our architecture, so I stick with that. The same thing, yeah. But what it does is using past APIs again, and then what it offers is effectively collapse some of the API that we have for Maximo.
Long story short, because I think it's important to doing this and I did the kind of the headline result in terms of the workflow, kind of a, we, this is the kind of a success rate compared to one-to-one versus
kind of abstraction layer. So you can see the success rate will be a lot more better. ToolsOrToys will be a lot smaller. The key thing is then is the average tokens and latency as well. So the average token you use will be less. And then the cost that you pay for it is also be less.
So, I think if if this is kind of the evidence that you want to put into your ADD or KDD for you to use them, the thing is like you can you can rerun them as you got the eval code running here, you can rerun them as well, but at least then you have something quantifiable that you can present it and say, "Yeah, we've done this approach, we we evaled it and we have something that
576072292608
Emma Sun   14:32
No.
576072292608
Ha Duong   14:32
If valuable, we can show it to the team.
576072292608
Mike Agar   14:35
And this is about, this is about merging APIs together, right? This is about not giving the tool 20 APIs, but giving it one that does 20 things.
576072292608
Ha Duong   14:40
That's right, yeah.
No, it depends on what these workflows. I think you have to be thinking about what, how do you abstract it on these layer.
Like that, ohh, sorry, not there here, yeah, on this layer.
So basically what I have here, I have a container hub environment and you have the maximal here. So but what I'm saying is, in order to implement this abstraction, you got this abstraction layers on here. Now, how would you want to do it? How do you, what is the best way to curate it? There's a few kind of best practise that I can, I can share.
But on a high level, it's basically instead of export one-to-one API call, you abstract it at this layer. And then once you have that others layer, you can expose that within API management.
576072292608
Emma Sun   15:35
How can you put this repo in the chat?
576072292608
Ha Duong   15:38
Yeah, I can put that in the chat. Yeah, sure. Yeah.
576072292608
Emma Sun   15:39
OK, thanks.
576072292608
Ha Duong   15:41
Yeah.
So, did you should have a bicep?
And a code for the application, and then the eval that you need to go as well.
But I think the reason I did it is because I think last week, I think we understand the high level concept of what I'm trying to say, but we don't have anything that number wise that I can prove. So I said, let's run it. Let's actually run it.
576072292608
Emma Sun   15:53
Mhm.
Mm.
Mm.
Yeah.
576072292608
Mike Agar   16:06
It's still an area I'm concerned about, right? Because I get the concept, I get the idea that the less you give it, the better, the smaller the context window is and therefore the more accurate it is to run. My concern is we've invested considerable amounts in a standard API set.
576072292608
Emma Sun   16:06
This is good.
576072292608
Ha Duong   16:18
Yeah.
576072292608
Mike Agar   16:25
And the idea we start to orchestrate something on top that enables that to be exposed as a single API.
Essentially.
576072292608
Ha Duong   16:36
I'm not saying it's a single API, so I think it just basically what you want to ask the MMC to do.
Right, then because MMC can explore one or more tool.
576072292608
Mike Agar   16:47
Yep.
576072292608
Ha Duong   16:47
So I'm not saying you have to have one single API that do everything. I'm just saying don't expose very granular API at the maximum level. Do it more abstractions. Imagine if you, my machine is just really slow on responding to my mouse. Here we go.
576072292608
Mike Agar   17:06
If.
576072292608
Ha Duong   17:10
is, I'm not saying here in here you have one single API. That's not what my message is. My message is here is very likely you will find that the API at this level will be very granular, very verbose. What do you want it? Do you want to provide some abstraction on top of it? Now it could be
576072292608
Emma Sun   17:28
Mm.
576072292608
Ha Duong   17:30
Instead of...
576072292608
Emma Sun   17:30
Yeah.
576072292608
Ha Duong   17:32
So, I think 14 in this scenario, and then the expo and said the other one was 7, right? You cut that by a half.
576072292608
Emma Sun   17:35
Yeah.
576072292608
Sourabh Sardesai   17:37
I think, in a way, I think we're already doing this, so we're already creating an abstraction there on top of basic core Maximo APIs, and then exposing that. So, basically, where we have written past API, we have used function apps, but also now we are using fast APIs as a...
576072292608
Ha Duong   17:41
Yeah.
Okay, cool.
576072292608
Emma Sun   17:43
Yep.
Yeah.
576072292608
Sourabh Sardesai   17:59
As a as a layer, as a layer of tools which we might have, yeah, and and...
576072292608
Ha Duong   18:01
Yeah, if you already have that, then yes, is is is a.
576072292608
Emma Sun   18:02
Yeah.
576072292608
Sourabh Sardesai   18:05
Exactly, and those fast APP endpoints will be then exposed as will be registered into a pin, and that the old goal is to then use a pin's out-of-box MCP converter to use it as a, you know, expose it as a MCP; otherwise, what we are saying is completely aligned, they are aligned with.
576072292608
Ha Duong   18:11
And.
576072292608
Emma Sun   18:11
Mhm.
Yeah.
Yeah.
576072292608
Ha Duong   18:24
Cool. Yeah, so.
576072292608
Mike Agar   18:26
So I think this is really, we need to focus on this, don't we? Because we've got to make sure we don't bloat the context window. It's like a principle that I think we need to register and be very cognizant of. I guess my concern is just in reality, how are we going to set a guideline around this? Because what I don't want to do is set a guideline that every API needs to be somehow
576072292608
Ha Duong   18:36
Veitch.
576072292608
Francisco Cachado   18:38
Yeah.
576072292608
Ha Duong   18:39
Yeah.
576072292608
Mike Agar   18:46
wrapped or re-engineered to be simpler because it feels like that's a guideline that is going to be impossible to work to, right?
But I guess we just have to set a principle and work around it.
576072292608
Emma Sun   18:55
Mike, I hear you, but I don't think that's easy to set a standardised guideline across use case like at this granular level. I think what ASUE should design is a big direction that we just aligned, you know, like APP and deploy MCP server, we don't use a separate container.
container to deploy MCP. And this doesn't deviate from the big direction we just aligned. Like, I think this is very at a use case level. Like when we think about domain-wise implementation, we need to make a decision at a use case level to say, you know, for this.
For this usage, we need to balance both the context window as well as, you know, don't give multiple endpoints to an agent. That's also very hard for an agent to manage. So there's a balance there, but I think those decisions can only be made at a use case level instead of have an overarching.
Principle.
576072292608
Mike Agar   19:59
They can, but they overlap, am I right? When, Sourabh, when you showed us this in APP, you showed like one API that actually had like 20 things in it, right? There were 20 different operations within the single API, and you published the single API as an MCP server.
576072292608
Sourabh Sardesai   20:18
Yes, but then, yeah.
576072292608
Mike Agar   20:18
So are we saying those 20 operations now become part of our context window?
576072292608
Sourabh Sardesai   20:22
No, only those which you select them, not all of them.
576072292608
Emma Sun   20:23
Oh.
576072292608
Mike Agar   20:28
But then we're limiting discoverability. If we're saying, well, only the ones you turn on, now you have to turn them on, which means it's no longer discoverable.
576072292608
Sourabh Sardesai   20:28
Orla.
So you do, that's why where that's where when harsh the the layer of you know using granular using multiple granular APIs and creating one functionality let's say which is more supportive. That's where that will come in picture.
And you might have another set of APIs. So there will be a granular level out core APIs that create a work order create. Yeah, that will be granular set. On top of it, we'll have another set of APIs, which will be more efficient, I would say, more efficient, more group.
576072292608
Ha Duong   21:04
Yeah.
576072292608
Sourabh Sardesai   21:17
And on top of that, there will be an MCP server which will be exposing that grouped efficient set of APIs, and that's what Agent will be leveraging.
576072292608
Ha Duong   21:27
So, just to paint a bit more detailed picture, this is the all the API that I mark on the Maximo API, so 14 of them, and then the the MMC only expose 7.
Yeah, so, and then I did expose, for example, find my work order, and what it does is you go a call to call slash ID, and then if you do a bit more complicated, so get work, get work order contacts, yeah, so MFM think about this, it actually doing multiple calls.
576072292608
Emma Sun   21:45
Helio.
Mm.
576072292608
Ha Duong   22:04
Yeah, so we get this lab work logs and so on. Yeah, so if you do one-to-one, the agent will then have to chain, how many calls is it? One, two, three, 4, 5, 6, 5 all together, right? So I can accomplish one task, where if you abstract that at the MCP layer,
576072292608
Emma Sun   22:05
Mhm.
576072292608
Ha Duong   22:24
Then from the agent perspective, that's one call. And then behind the scene, they do these things. And you know, is the right way to go. So yeah, that's kind of the structure that I'm trying to sell.
576072292608
Mike Agar   22:41
Yeah, and I guess my point is, we...
we have what we call our standard Maximo API set. And if we're going to build an abstraction layer on top of it.
576072292608
Ha Duong   22:48
Yeah.
576072292608
Mike Agar   22:52
I'm wondering what that does to our standard set. Should our standard set now become the abstraction layer, regardless of whether it's an Agentic use case or not? Is this an abstraction layer purely for Agentic? You know, we now have a whole new potential. I mean, maybe I'm exaggerating the, but it feels like we're building a different API layer for Agentic, which is not.
576072292608
Sourabh Sardesai   23:03
But.
No, so...
576072292608
Chris Snowden   23:09
Of.
And we can't really change the original work, can we, because we've got so many things using it. You know, we've got external clients who use it, we're not going to change all them, we're not going to change Aria, you know.
576072292608
Sourabh Sardesai   23:12
And what?
Exactly, yeah, yeah.
576072292608
Ha Duong   23:21
Yeah.
576072292608
Sourabh Sardesai   23:21
Ah, yeah, exactly. Ah, yeah. And and and even if so we have a KPM extraction level, it's not doing too much of not logical changes, just filtering, just allowing you to do queries in multiple ways. But in a way the functionality is going to unmapped with what maximum is.
Right.
The payloads are changed, which are more suitable for applications like Aria, make it lightweight, make it fast.
as compared to what X core Maximo APIs are. I think in a way that's a replication of what already Maximo does. But what we are talking in terms of agentic world is, for example, I'll give an example. Okay. So what I've done with the create SR, so I've created another function on top of
576072292608
Ha Duong   23:54
Mm.
576072292608
Sourabh Sardesai   24:09
what Maximum create SR, AI, API is right. What I've done is I've added a duplicate cheque into it. Yeah, the duplicate cheque does is like it at the first instance it tries to create an SR, maximum as a philtre cheque philtre and gives you back a set of SR which can be potential duplicates. But if I'm not looking into it.
syntax descriptions. So what this layer does is now it also does some LLM calls here and there and do some smart stuff so that you know it identifies which are actually the correct ones or not. So basically it's grouping duplicate cheque and create SR APP together and then making creating just one endpoint.
one simple payload and it will get it get work done. Another thing which we have done is with the API, which APP is exposing at the moment, the AI is maximum equipment. It allows only one SR to be created at one time. If you send a set of issues together, it won't create
multiple SRs. You need to hit that every single time. For this abstraction there, if you have created on that, you can just pass on a list of all the SRs you want to create and in one response it will create everything in the back of it and it will give you the complete collaborative response. So that's some examples I would like to
This is what the...
I think that would be.
576072292608
Mike Agar   25:33
But does that kind of mean, Sarah, we're building new API endpoints every single time we build a different type of solution that, you know, we're building specific API endpoints every time?
576072292608
Sourabh Sardesai   25:41
Okay.
576072292608
Francisco Cachado   25:43
Yeah.
576072292608
Sourabh Sardesai   25:44
So, so this set of two, this set of abstraction is now good by three agents, you know, Aviva, and Barry. So it was built in such a way that it could be used across multiple similar agents.
576072292608
Ha Duong   25:44
Burt.
Mm.
576072292608
Sourabh Sardesai   25:57
So in a way, that's what tool building is, right? You can build a tool which can be used, build a tool in such a way that it can be used by multiple agents in a similar way. So we just expose the open APP spec for that tool and the rest of the agents can then just use that in the registry and create.
576072292608
Ha Duong   26:00
Hmm.
576072292608
Mike Agar   26:14
It's just, it's quite a big, for me, that's massive, right? Because we're basically saying that we're going to build brand new an AIAgentHelpdesk API set, which can be used by agents on top of all of our existing standard APIs we have for Maxima.
576072292608
Sourabh Sardesai   26:25
If required.
So that's why it it that's again it I think it it's required, but otherwise we can still expose the core APIs as a as a open APP spec, which we discuss and integrate, so not always MCP, but we can also expose the core MCP as well.
576072292608
Emma Sun   26:33
Hitesh.
576072292608
Mike Agar   26:43
But I guess that's then where we're in the grey area, right? When should we do this and when shouldn't we? How do you know whether we're going to be enforcing that they go off and build a new API versus using existing ones? You know, how do we...
576072292608
Ha Duong   26:44
Yeah.
576072292608
Sourabh Sardesai   26:47
Yeah, yeah, yeah, yeah, yeah.
I think, I think that.
576072292608
Ha Duong   26:56
Can I just jump in and suggest something different? So one of the principles I really like is maximise the work not done. I'm not sure you're familiar with that phrase, but if I apply the similar principle here is we understand there's a benefit to have this abstraction layer. We don't know what is the best way to implementing it at the moment.
576072292608
Sourabh Sardesai   26:58
Yeah.
576072292608
Ha Duong   27:18
So we can document it, the principle is we will have this layer in place, right?
So, we put this layer in place, we we done we done the quantifiable thing, we know is giving us value, right? So, we we have that, so we say, right, okay, yes, instead of having a direct expo, a very, because at the moment you can expo directly from the Maximal API straight to APP, and then MCP will be immediately available.
What I'm saying is, how about we put this layer in here? So that is our principle. Now we can say, we say, if we follow the maximizer, we're not done, we say, okay, in the principle, we expose this V1 of the MMC server of a one-to-one relationship, right?
We got this abstraction layer, and then what we do is then we try it out. If we see the abstractions that needed, then we can implementing at the latest day, but we got the place for it instead of go direct, and then we don't have any place to change. Now, the reason why I do this example down here,
576072292608
Emma Sun   28:17
Thank you.
576072292608
Ha Duong   28:23
Because when I do some research about the API and the workflow, these kind of things are common from my understanding of what I, the work we can do with Maximal API.
But I don't know your, I don't know the use case that we are doing here, right? So I think if we agree in principle that, okay, we want to ask people to have this placeholder in place, right, on the most simplified version is a one-to-one until we know we feel the pain, we know the workflow, then we can abstract it.
576072292608
Emma Sun   28:57
Um, yeah.
576072292608
Ha Duong   28:58
Is that something that you've been happy with?
576072292608
Emma Sun   29:01
I think Mike is asking also more than just Maximal. I think Max's question is more like, when should we group things, group the APIs together? Like what are the decision criteria, right? Like we decide whether this is a standalone API or this is a group.
576072292608
Mike Agar   29:15
Blue.
576072292608
Emma Sun   29:22
And what's up, yeah?
576072292608
Mike Agar   29:22
But I think I think what what Ha is saying there is is actually don't make that decision, publish it separately and then you can make that decision later.
576072292608
Ha Duong   29:30
Yeah.
576072292608
Mike Agar   29:31
But then you're publishing it separate. So this is what I think you're saying hard, right? As a stage one. So we have Maximo with a bunch of APIs.
576072292608
Ha Duong   29:38
Mm.
576072292608
Mike Agar   29:38
We have already exposed those APIs through AIS. Now, there might already be some level of orchestration in some of those APIs, right? So some of them might have already abstracted away. I'm guessing a lot of them haven't, right? So we've got, let's, you know, a set of APIs now exposed to AIS, which things are already using, right? Systems call them, customers call them, third party systems call them.
576072292608
Ha Duong   29:45
Mmh.
576072292608
Mike Agar   29:59
they're in use. What I think you're saying is that we should wrap these up, expose them separately, so that maybe one day or maybe on initial release, right, this will be a use case decision, you can do this potentially and start to further abstract and align them so that agents only have to deal with
A simplified API set.
576072292608
Ha Duong   30:23
The AIS is in your control.
576072292608
Emma Sun   30:27
Tew.
576072292608
Ha Duong   30:28
In Jordan.
576072292608
Sourabh Sardesai   30:28
But it has a wider impact. So we can't just go and change anything in ANS because they are used across multiple systems.
576072292608
Ha Duong   30:33
Yeah.
So I think if it is in your control, then I think I understand what, I think I understand what Mike is saying is we got, we already have these kind of abstraction layer or potentially abstraction layer. Ideally, we should not have another abstraction layer on top of the abstraction layer, which I think I think I'm I think that makes.
576072292608
Francisco Cachado   30:56
Yeah.
576072292608
Ha Duong   30:57
completely sent. So what we can for this one, the abstraction layer that I mentioned here, it actually your AIS in this diagram. Now, if you want to reuse AIS and expose the MCP server directly, you know, feel free, because that is that basically my message here is you should have abstraction layer. If you already have one, don't make another one.
Then, then, OK, so I think we are all on the same page here. Now, in the scenario in the future.
576072292608
Mike Agar   31:19
Burt.
576072292608
Emma Sun   31:19
Yeah.
576072292608
Chris Snowden   31:20
Hey.
I'm glad you said that. I just, I didn't, I don't quite understand what the abstraction layer is, given that we have APP, which has it abstracts them as pretty.
Pretty abstract as it is. I'm struggling a little bit.
576072292608
Ha Duong   31:35
Yeah, the APP, what it doesn't do is, for example, in the example, the workflow here is that APP don't tend to do kind of a call an API, get the API, get the outcome of this one and change it to another one. APP will be kind of thin layer kind of.
576072292608
Chris Snowden   31:49
Yeah, but yeah, that's not its job. It's a one-on-one, it's a transactional synchronous.
576072292608
Vincent Rouet   31:51
Mm.
576072292608
Ha Duong   31:53
Yeah.
Yeah.
576072292608
Chris Snowden   31:58
That's its job, and that's why it's positive.
576072292608
Ha Duong   32:00
Yeah.
576072292608
Mike Agar   32:00
But that's just a PIM. We do absolutely have.
I didn't logic apps function apps in here that do this type of orchestration behind the scenes, right? So you call the API and it might call 2 APIs behind the scenes.
576072292608
Ha Duong   32:08
Yeah.
576072292608
Mike Agar   32:15
That that is in there, right? Like, like document links and stuff, right? So, so that that's kind of that's exactly what I'm saying, right? Why do we need multiple?
576072292608
Ha Duong   32:16
Yeah, yeah.
576072292608
Vincent Rouet   32:16
Yeah, you.
576072292608
Ha Duong   32:22
No, no, no. I misunderstood that you don't have an abstraction. I'll connect that directly to the maximum API, right? So my ACA in this diagram is your AIS effectively.
576072292608
Chris Snowden   32:33
Yeah, OK.
576072292608
Mike Agar   32:34
Okay.
576072292608
Ha Duong   32:35
Yeah, so, so I think we are on the same page here.
576072292608
Mike Agar   32:39
So I think what, therefore, what I think we're saying, right, is in general, we're going to end up using the standard APIs because they're standard for a reason, right? Hopefully they're sensible unit blocks of API calls. If they're not, and there's 500 APIs and they're not well structured, I feel like we just have a more fundamental problem. If our APIs are badly designed, then we should restructure that. We might have to look at restructuring them.
576072292608
Ha Duong   32:50
Mm.
576072292608
Sourabh Sardesai   32:54
But...
576072292608
Ha Duong   32:59
Yeah.
576072292608
Sourabh Sardesai   33:00
But with this AIS layer or this abstraction layer, from what I know, we are still using all those APIs which Maximo is giving out. So how are we saving the context window by doing this?
576072292608
Mike Agar   33:01
In the normal way.
Well, that's kind of my concern, Sarah, because I guess therefore...
576072292608
Ha Duong   33:19
Yeah.
576072292608
Mike Agar   33:23
I can't see us doing much. We're going to take what we've already got and we're going to reuse it. And if that's lots of API calls that are individually passed through.
Well, I guess that's what we're going to end up using, right? And is that a problem?
576072292608
Sourabh Sardesai   33:35
So what I feel is I still need, for example, there are like 10 APIs which are on APP and AI, out of that we might need only four. So instead of just exposing them, all of them, you might use a MCP wrapper for this AI.
and only expose those four of them and create that MCP endpoint. You might have multiple MCP endpoints which might have groupings of all these APIs as required for the project and we might have multiple MCP endpoints. That's what I think will end up.
576072292608
Mike Agar   33:59
Mmh.
576072292608
Ha Duong   34:05
Mm.
And.
I think because you already have the abstraction layer, and this is why my question is about who owns these AIS. And if the answer is you own it, right, then when you see the problems that you need further abstractions, then you can implement it yourself and you can then use that to expose as an MGP server by APP.
576072292608
Mike Agar   34:20
A.
Yeah.
576072292608
Ha Duong   34:31
So yeah, my message here was basically purely was have an abstraction layer, which you already got, then use those. You don't have to do further if you need. Yeah, exactly that. Yeah. So if you need that kind of thing later on, then you build it yourself, you then can explore it quite quickly to.
to other consumer. And at the same time, you don't break other people work, right? The existing API still exists, still function.
576072292608
Vincent Rouet   35:04
But how the AIS layer is not just API management in the green box, it's AIS for the endpoint, API management for the endpoint, and either a function or a logic apps for the logic.
576072292608
Ha Duong   35:09
No, I think there's underlying the logic app.
Yeah, so the abstraction you can put on the logic app or the function or in the diagram that I'm calling out here is ACA compute is irrelevant.
576072292608
Vincent Rouet   35:20
Yeah, OK.
576072292608
Mike Agar   35:20
Yes.
576072292608
Vincent Rouet   35:29
Yeah, so, and I think that the question as to when do you, because this is a model that is known as system API, process API, and experience API. You create three sort of layers of API calls. So in this case for the MMC, why can't you just create that new MMC and that new logic?
576072292608
Ha Duong   35:31
Yeah.
Yeah.
576072292608
Vincent Rouet   35:50
whenever you come across, you know, through experience, you realise that a specific process calls upon Massimo API too much, so you need to optimise a context window. Therefore, you create a new aggregator that you deploy. So it's sort of a on demand as opposed to.
Too much anticipating on the future requirements.
576072292608
Ha Duong   36:15
Yeah.
Oh.
576072292608
Vincent Rouet   36:17
Sh.
576072292608
Mike Agar   36:17
It is just going to be right. So because our option is use the existing APIs and expose them through MCP, which now means that the agent has three tools to deal with. Or should we build the new API, which takes all three and converges them into one if possible, right? Let's assume it's possible.
576072292608
Ha Duong   36:21
Yeah.
576072292608
Vincent Rouet   36:22
Yeah.
576072292608
Ha Duong   36:25
Yeah.
576072292608
Mike Agar   36:33
and then have MMC only use this. Now the agent in theory gets a bonus. But now we're in a weird position, right? We've got customers calling 3 arguably legacy APIs. We've got a nice new snazzy one here.
576072292608
Ha Duong   36:33
Ha.
576072292608
Emma Sun   36:40
Ha.
576072292608
Ha Duong   36:44
Mm.
576072292608
Mike Agar   36:47
Just.
That's what my concern is, right? How do we know when to even do this? And if we do do it, we kind of got some, we're almost creating technical debt. We have to clear this up at some point, right?
576072292608
Vincent Rouet   37:01
But you need to decide today.
576072292608
Ha Duong   37:01
Yeah, yeah, I think that this is very use case specific, right? And that we can use like unit of words and so on. I don't think that we can give a clear guidance without knowing the actual use cases. So that's why I reiterate my message about the maximise that we've not done.
576072292608
Emma Sun   37:08
No, exactly, Mike.
576072292608
Mike Agar   37:08
Yes.
No.
Yeah.
576072292608
Ha Duong   37:21
where we do the minimum required because we know we've got this abstraction layer available. So we know that we can move for further abstraction if needed, right?
576072292608
Mike Agar   37:21
Yep.
Yep.
So it's almost hard something, you know, if we built, and we're going to be iterative here, right? So we're going to build some agents. And over time, if the MCP gets more and more APIs built into it, at some point, we might start to see deterioration in response quality. And at that point, we can start to say, hang on a minute, this might be due to context window flooding, whatever the technical term is.
576072292608
Ha Duong   37:37
Yeah.
Yeah.
576072292608
Mike Agar   37:52
And we start to say, on we, you know, we might need to start to look at does reducing the number of API calls here make a difference to accuracy.
576072292608
Ha Duong   37:59
Yeah, so I think that the KDD that we're saying is we have the abstraction layer in AIS, we want to utilise it. Our principle is maximizable not done, so reuse as many existing APIs as possible with the decision that we open for options to reevaluate.
576072292608
Vincent Rouet   37:59
Yeah.
576072292608
Mike Agar   38:13
Yep.
576072292608
Ha Duong   38:19
if we see performance. But I think now understand that we have the AIS, then that makes sense for me. When I think last time when you showed the diagram, there's only APP. I forgot there was another layer of function you got. And that was that was that was my message. I need something that do these abstractions.
576072292608
Mike Agar   38:20
Yeah.
Perfect.
Yeah, we're no, we're we're terrible about that. Okay, okay.
576072292608
Ha Duong   38:39
Okay, cool.
576072292608
Mike Agar   38:40
Yeah, sorry, we have a terrible habit of just lumping. Well, I have a terrible habit of lumping APP and AIS together and sort of talking about them as though they're the same, the same thing. OK.
576072292608
Ha Duong   38:45
No, that's not my fault.
I should clarify that. I think we'll be good, yeah. Sorry, I do got a jump, but I think we are concluded on the MCP server. You got Vincent here, so...
576072292608
Mike Agar   38:59
Yes. So just to summarize, right, we're saying.
AIS is the is the is the layer we're going to use both for any orchestration if we need to merge things together, but we'll do that, you know, as we go use case specific. In general, we'll be exposing our existing APIs through MCP, which AIS handles for us.
576072292608
Emma Sun   39:20
Gregory.
576072292608
Mike Agar   39:20
Full stop.
576072292608
Ha Duong   39:21
Everybody happy?
576072292608
Emma Sun   39:22
Amazing.
576072292608
Mike Agar   39:23
Okay, fantastic. Thanks, Ha.
576072292608
Ha Duong   39:24
Bye, see you soon.
576072292608
Emma Sun   39:26
Anshul.
576072292608
Mike Agar   39:31
So, yeah, great.
576072292608
Emma Sun   39:31
All right, we have 20 minutes more. Sourabh and Francisco on domain segregation. Is Francisco still on? He is not. Okay, Sourabh, do we align something solid for the domain segregation from last call?
576072292608
Sourabh Sardesai   39:49
No, actually, I didn't get the chance to.
HOP device can include.
576072292608
Mike Agar   39:57
So, I think we had a solid proposal, didn't we?
576072292608
Sourabh Sardesai   40:02
Yeah, at the moment what we were trying to do is we create a resource group for every domain dev desktop. That's what we would. That's what we are. I think we're trying to impose. We're not creating different subscriptions per domain, just we have dev subscription and.
Um, production subscription.
There is also legacy test, pre-prod and prod, but I'm not sure whether we want to use that.
At the moment, so far, whatever we've done on the agentic front, we've used non-prod and prod. Out of that, non-prod subscription, we've got dev, this is group, test, this is group, and then production.
So we would be doing this similar, yeah.
That's correct.
Yeah.
576072292608
Mike Agar   40:55
Vincent, you had a much better diagram that I've just read on here. I think you had a good one, didn't you? We kind of had the same thinking, I think, around the domains, but you introduced the concept of sort of the central hub for model, you know, where the models would live, etc. So
576072292608
Vincent Rouet   40:56
I think.
Yeah.
576072292608
Francisco Cachado   41:24
Mhm.
576072292608
Vincent Rouet   41:26
Well...
576072292608
Francisco Cachado   41:26
Mhm.
576072292608
Vincent Rouet   41:27
Because typically, yeah, our recommendation is...
576072292608
Francisco Cachado   41:28
Ed.
576072292608
Emma Sun   41:32
Hello.
576072292608
Vincent Rouet   41:32
Because your subscription is...
576072292608
Francisco Cachado   41:33
Here, here, it's it's where, here it's where like certain needs like certain might you need like to to give us like the view, because like the current like setup for like this domain segregation is that we only have one subscription and then in and and then in we'll have one resource group.
576072292608
Sourabh Sardesai   41:48
And multiple.
576072292608
Francisco Cachado   41:53
For domain slash environment.
So it will not meet with what Vincent is on the screen. So we need to like, like we need to have that view to understand if we can move to a solution like this, where we have like more segregation and you can implement like an urban spoke approach.
576072292608
Mike Agar   42:05
Yeah.
576072292608
Francisco Cachado   42:18
Or if we are tied up with the current system that mighty uses for all the environments.
576072292608
Mike Agar   42:27
And I guess it's back to why we even think we need domains, right? Because when I was thinking about it after the meeting, this is where I was suddenly getting confused. You know, what does the separate domains actually give us? Why is that segregation important? Agents can still talk across them. I know there was some advantage in kind of data access control to some extent, but it has to flow across domains anyway.
576072292608
Francisco Cachado   42:45
Yeah, so...
Yeah, exactly. So the thing is, exactly as you said, Mike, so here there are like the two sides in like confronting each other. Like if we have an urban spoke, we can put like a lot of like things that are spread across all the, for example, if we are looking only for EFF, we can have just some resources that will be static.
for all the environments. So we can have them in the hub and then each spoke network just connect with the main one. But that is not the current way MakingItHappen does. So this would be good like to 1st to align and decide which would be the best.
approach, because for now, the infrastructure that we have in place is based on the mighty ways of creating the infrastructure, but more than happy to like change to this approach.
576072292608
Sourabh Sardesai   43:44
But I think this is what we have right at the moment, what Michael is what Mike is showing at the moment. This is what we have one subscription for a dev, for let's say call it non-pod, yeah, and then we have.
576072292608
Francisco Cachado   43:47
Mmh.
Yeah, it's, yeah, run it.
576072292608
Sourabh Sardesai   43:58
Yeah, and we have dev, test, dev, test, not product. Can we remove product from that? So dev, test, and one subscription.
576072292608
Francisco Cachado   44:03
The.
Quick question, sir, is this is this me or I cannot hear you very well? I don't know if other if others are having the same problem, but I cannot understand.
576072292608
Mike Agar   44:13
Yeah, you're not coming through. Great. Sandra.
576072292608
Vincent Rouet   44:14
Yeah, you're coming through your earpiece and it doesn't come very, very well, the sound.
576072292608
Francisco Cachado   44:20
So, sorry, sorry, sorry, if you can just change with this. Yeah, much better. Yeah, much better. Thanks.
576072292608
Sourabh Sardesai   44:21
OK, can you hear me? Can you hear me now? Yeah, sorry, sorry for that. So, so basically, yeah, this is 1 subscription which, let's call it as a non-product subscription. Yeah, within that non-product subscription, we have dev and test per domain resource group, so one.
576072292608
Francisco Cachado   44:40
Mhm.
576072292608
Sourabh Sardesai   44:41
Research group for EFF Dev, one resource group for EFF Test, one resource group for HR Dev, one resource group for HR Test.
576072292608
Francisco Cachado   44:46
Is it?
Mhm.
576072292608
Sourabh Sardesai   44:50
Yeah, and then the idea is to again replicate one resource group each in production for HR prod, EFF prod, sales prod.
576072292608
Francisco Cachado   45:03
Nick.
576072292608
Sourabh Sardesai   45:04
That's what we are trying to do at the moment. And by doing this, we can easily segregate the costing of each domain because every resources we are creating are tied to one resource group and we can get a resource level and resource group level utilisation cost and everything.
576072292608
Francisco Cachado   45:07
Mhm.
576072292608
Sourabh Sardesai   45:22
You know, and controls as well, and control put access policies across users groups. So, in terms of that, we have, we are achieving what we need to, unless...
There's only one thing which which I am looking as a bottleneck, but...
That, that, that's your booking limit, so I think it's limited to a subscription, and other than that, I don't see any any any problems at the moment.
I think it was a little.
576072292608
Mike Agar   45:56
I guess with all of these things, right, it's best practice. I don't want to base it too much on what we do today. If what we do today is wrong, let's change it, right? It's trying to get to.
576072292608
Francisco Cachado   45:56
Thanks.
576072292608
Sourabh Sardesai   45:58
Yeah.
Yeah.
576072292608
Francisco Cachado   46:02
Yeah.
Yeah, Mike, Mike also copied the ai app for the production subscription.
576072292608
Sourabh Sardesai   46:04
Yeah.
Yeah, yeah.
576072292608
Mike Agar   46:09
We're using this already then, because I was going to ask that. So this is already there, Sourabh, is it a central? Okay.
576072292608
Sourabh Sardesai   46:13
Yeah, yeah, yeah, yeah, yeah.
576072292608
Francisco Cachado   46:15
Like, like, for now, so for now, we have all the LLM hosting inside of each resource group, that's that.
576072292608
Sourabh Sardesai   46:21
Uh, actually, we, yeah, so we usually...
576072292608
Francisco Cachado   46:24
That's why I'm asking, because currently we don't have this system in place because of the restrictions. But if we are happy to move to this approach, I'm also, like, I'm very keen to have this system of putting resources that can be shared.
576072292608
Sourabh Sardesai   46:39
So.
576072292608
Francisco Cachado   46:43
Outside.
576072292608
Sourabh Sardesai   46:43
So, OK, sorry, so the AI have, uh, let's call it Foundry Mike and Foundry is...
576072292608
Francisco Cachado   46:49
Mhm.
576072292608
Sourabh Sardesai   46:50
Each resource group has its own foundry.
OK, so it's not shared across HR EFF cells. Each each resource group has their its own foundry.
Singh.
576072292608
Mike Agar   47:05
But wasn't that the challenge that Vincent gave us? Was the best practise is to have a central hub where the models live, and then when you update the model, you do it once, not three times or 10 times.
576072292608
Sourabh Sardesai   47:11
So, so, so...
So, then we have a problem of rate limit.
576072292608
Vincent Rouet   47:18
Yeah.
576072292608
Sourabh Sardesai   47:25
You might, you might end up with the little issues, yeah.
576072292608
Francisco Cachado   47:30
If, if we.
576072292608
Vincent Rouet   47:30
But that's why you've got different policies where you can deploy multiple domains. You can deploy multiple instances even in your hub. When you say the hub, it doesn't mean just one deployment of.
576072292608
Sourabh Sardesai   47:30
Right, so it's like, yeah, so, yeah, and there's no, we're not talking about for training.
576072292608
Francisco Cachado   47:33
Mhm.
576072292608
Vincent Rouet   47:44
There's some background noise coming through. Yeah, it doesn't mean just one instant of Foundry. It can be multiple, but it's through the load balancing of the models through the hub that you get this rate limiting issues.
576072292608
Emma Sun   47:58
Yeah.
576072292608
Vincent Rouet   48:01
Addressed, yeah.
576072292608
Sourabh Sardesai   48:05
So, so do you propose that we should have only one AI hub for all non-product domains? Because at the moment we don't, we have separate foundry for each resource group.
576072292608
Vincent Rouet   48:22
No, so this is one shared, one maybe one shared for dev and one shared for test. Or you could have one, yeah, one instance, one hub for all the dev tests. I think.
576072292608
Sourabh Sardesai   48:28
We.
576072292608
Vincent Rouet   48:35
Um, so what, what's the so when you said rate limitings?
Having too many, too many queries on the same model deployments.
Okay, because when you deploy one model, so it doesn't mean you're actually deploying less model. It means you're deploying the number of models that you need. So you make sure you have enough rate, you have enough.
576072292608
Sourabh Sardesai   48:47
Yeah.
576072292608
Francisco Cachado   48:58
Mhm.
On that.
576072292608
Vincent Rouet   49:00
But they all manage, they all deploy centrally as opposed to each instance is deploying their own model. So, you know, 5 instances deploying 5 GPT-5 versus one instance where you also deploy 5 times GPT-5.
576072292608
Francisco Cachado   49:09
Mmhm.
Okay, on that device, and just to do like just a parallel question, what you just mentioned about TPM and RPM? All those settings can be done, like I know that we can change them on the UI, but if there are necessity to increase them even more, it's a possibility with Microsoft if it's needed, like with...
for the production environment. If we like, if we move to approach where we have a centralised AI hub with everything, if we have everything running inside of the same hub, we might we might reach a point where like the TPM and RPMs are not enough. It's there a possibility to increase those limits with Microsoft if needed.
576072292608
Vincent Rouet   49:58
Yeah, it's possible to increase the limits, but this is also where you would put some failover patterns on the API management side to go over to a new, and this is probably where I think we need to revisit this, because this is probably where having one subscription might actually be a limitation, so...
576072292608
Francisco Cachado   50:00
Okay.
I should be done.
Mhm.
576072292608
Vincent Rouet   50:18
I think, yeah, we need to look further into this because Sourabh today, I'm still not sure why Mighty wants to limit, I mean, subscription is free, right? So, and subscriptions give you even more security and billing boundaries, right? So
576072292608
Francisco Cachado   50:19
Is it?
576072292608
Vincent Rouet   50:39
It's always about minimising the blast impact. You know, if one subscription is compromised, it's only one set of workload in that subscription which are compromised as opposed to, you know, I mean, I don't know how your networking is done, but the more segregations you're doing, the more part...
But you know, separation you're doing, the less impact you have from a security standpoint. So still not sure today why mighty model is to minimum number of subscriptions.
576072292608
Emma Sun   51:00
Yeah.
576072292608
Sourabh Sardesai   51:01
So.
Please.
Yeah, I think there is a wider discussion on that. But what are the...
576072292608
Francisco Cachado   51:16
Mhm.
576072292608
Vincent Rouet   51:17
OK, so it's not OK, so just to move forward, so it's not one we're going to be able to move in the coming days or weeks. If this is if this is what we have to work with, then then let's let me look at this hub and spoke approach for the for the models and and look at this rate limiting issue.
Should I do that?
Okay.
576072292608
Emma Sun   51:47
No.
576072292608
Vincent Rouet   51:58
Okay, so let's make note of this.
576072292608
Mike Agar   52:03
Oh, I was talking on mute then.
So are we talking here about whether this box goes across everything or is domain specific or are we talking about subscriptions and whether we have multiple? I'm slightly lost where we got to with all of that.
576072292608
Vincent Rouet   52:20
I think we're talking about how make sure that with this model where the box is across, we're not going to hit any token limits, et cetera.
576072292608
Francisco Cachado   52:21
Ha.
576072292608
Mike Agar   52:27
Limits and okay, yeah, yeah, so it needs to be scalable and even within a subscription you've got like failover and multi availability zones and things, right? So it's not like.
576072292608
Francisco Cachado   52:31
No.
576072292608
Mike Agar   52:41
You know, there's no reason we would need that from a reliability availability perspective, is there multiple subscriptions or anything?
576072292608
Francisco Cachado   52:45
Mhm.
576072292608
Vincent Rouet   52:49
Well, yeah, you don't go zonal deployment with Foundry, for example, so...
576072292608
Mike Agar   52:54
Okay.
576072292608
Vincent Rouet   52:55
Yeah, so if you wanted to have two models, one in Sweden and GPT-5 in Sweden, and another one in North Europe, if it's there, then you would need your API management to operate that, you know, load balancing between the two regions.
576072292608
Francisco Cachado   53:12
It.
576072292608
Mike Agar   53:12
Because these are KDDs, right? This is, do we want, you know, what availability are we targeting? Do we want failover?
576072292608
Francisco Cachado   53:13
Yes.
576072292608
Vincent Rouet   53:20
Exactly, these are questions, yeah.
576072292608
Mike Agar   53:21
We haven't even...
576072292608
Vincent Rouet   53:23
So, so, but this is gonna depend on the use cases, yeah.
576072292608
Mike Agar   53:27
It will, but I guess this Emma is kind of where we need to start surfacing that type of question, right? Are we...
I don't know what availability the these things have, and but but if we're if we're in an agentic world and we, you know, all of our mighty mighty is running on AI and we haven't built in failover.
576072292608
Francisco Cachado   53:45
Mm.
576072292608
Mike Agar   53:49
We're going to have a problem, aren't we?
576072292608
Francisco Cachado   53:53
Mhm.
576072292608
Sourabh Sardesai   53:55
And then how do we then limit the usage? How do we apply the policies, different domains? How do we set the quota?
for the different domains.
576072292608
Vincent Rouet   54:06
So, that's where you would have the some of the policies that will can inspect the header, see where it's coming from, and implement different throttling policies.
You can have token rate limiting policies in API management.
Are you planning on doing some billing of some sort, some chargeback or?
576072292608
Mike Agar   54:27
I, I guess it's...
576072292608
Sourabh Sardesai   54:28
At least accountability needs to be there. Yeah, each each domain will need to pay for their own expense, yeah.
576072292608
Francisco Cachado   54:29
Mm.
576072292608
Mike Agar   54:30
Yeah.
576072292608
Francisco Cachado   54:33
Yeah.
576072292608
Vincent Rouet   54:35
Yeah, because all traffic can be dumped into log analytics and then you can run some.
576072292608
Mike Agar   54:36
8.
576072292608
Sourabh Sardesai   54:39
In fact, in fact, we are also looking forward to get an agent-wise billing, because let's say if there are like 10 agents in EFF who are consuming like X amount, we need to know which agent is consuming how much that is.
576072292608
Francisco Cachado   54:53
No, but we will, but we will have that on, like, on the absolutely, we will know how many tokens each agent is spending, and then we can have, like, on the...
576072292608
Sourabh Sardesai   54:59
No, no, so token is one thing, yeah, but in terms of observability.
576072292608
Francisco Cachado   55:02
No, but like then we can, but then we can know from token the cost, like by the cost by by token, then we can we know which will the amount of money that that agent will.
576072292608
Vincent Rouet   55:13
Yeah.
576072292608
Sourabh Sardesai   55:14
Yeah, not, not, not just that. For example, if let's say if token, so one agent is consuming XYZX services as well, and it needs it, it has some hosting costs or it has some consumption costs, even that will be account data as a part of that agent, right?
576072292608
Francisco Cachado   55:27
Mm.
Yeah, yeah, but that OK, but I think that that is already like something that we can do ahead now is more like kind of like to to decide this subscription system and like are we going to segregate the entire thing, so or do we move with this subscription system that Mighty has in place?
That is like an end product and the product subscription, and like the FF HR sales will be living alongside.
other applications that MIT has, or do we create like proper subscriptions for HR and subscription for the FF and a subscription for for for sales? That is the other approach, or if we stay with or if you stay with this approach and like everything lives alongside other things.
576072292608
Sourabh Sardesai   56:12
In.
576072292608
Francisco Cachado   56:19
And then we just have to do peerings between each resource group, HR, EFF cells, to the resource group where we'll put the Azure Foundry.
576072292608
Sourabh Sardesai   56:31
Can we, can we, can I ask Vincent, what are the drawbacks of using this methodology, this topology of resource groups, dividing it into resource groups rather than subscription? So if the cons are too bad, then I think we need to.
576072292608
Francisco Cachado   56:46
The thing is like, reason can go a little bit more like, but one of the first things is like in terms of the permissions. If you have a subscription from scratch, like what happens sometimes when you have like this massive subscription, like you start to give permissions, EIM rules at subscription level and not at the resource group level.
So, you end up having resource groups that someone should not have access, but since it has access at the subscription level, it sees the entire thing. If we have proper subscriptions, we can manage the rules inside of port only for that subscription and not for the for those big ones, but Visa can also.
Uh, gives a view on this.
576072292608
Vincent Rouet   57:29
Yeah, and this is, yeah, as I mentioned, subscription is your is a billing is a security and billing boundary, so, so as you know, it gives you clear separations if you are, if you have no access, you know, if an HR think about.
you know, because you have one subscription, you need to start having some RBAC configurations on the resource groups in the same subscriptions where you might have some RBAC configurations where you also have HR workloads, right? So it's not impossible, but it's a lot of...
strict configurations and management of our back roles you have to do in your subscriptions. Well, if you're using two separate subscription, you by default having isolations, right? So it's out-of-the-box, it's isolation. So you're granting access as opposed to, yeah, having, if you think about someone inadvertently gets.
576072292608
Francisco Cachado   58:16
Mhm.
576072292608
Vincent Rouet   58:26
Um...
below owner is contributor access on the subscriptions. Potentially they can go and start reading those workloads of HR and sales. Again, yeah, I keep being myself here, but if it's completely separate subscriptions, the sales contributor roles will have no access whatsoever to an HR workload. So
576072292608
Sourabh Sardesai   58:41
It is not being there.
From, but you stop.
576072292608
Francisco Cachado   58:48
Mm-hmm.
576072292608
Sourabh Sardesai   58:49
Secret.
576072292608
Vincent Rouet   58:49
Then you have that continuity. So take the back end, the fabric, for example. So fabric might be, or your data warehouse using whatever you're using, might be a bit different because it might be in its own subscriptions in that case. Then you're back to security group.
Yeah, in terms of access, the subscriptions give you the security isolation and then it's the billing, right? So for most organizations, whatever we deploy in our subscriptions, this is our bill, this is what we pay for. Some of the teams, you know, they don't need to be some divisions of, well, I use the
10s of a percent of a egress quarter on that subscriptions or you know, so what is in this bucket is what I'm paying for. I'm not paying for anyone else type of thing. So, and the subscription again is free, right? So there's really no overhead over.
576072292608
Francisco Cachado   59:47
Mmh.
576072292608
Sourabh Sardesai   59:47
Yeah, so.
576072292608
Vincent Rouet   59:48
I'll be less instructed and be less clear on networking. Maybe one of my network colleagues could clarify whether subscriptions give as an impact from a network point of view, but yeah.
576072292608
Francisco Cachado   59:59
It, it's some of the same, because then the, like, all the network peering needs to happen at resource group level, but again, it's more that will give them like to have bring subscription specific for each for each domain.
576072292608
Sourabh Sardesai   1:00:16
Yeah, I think we had some, we had this discussion with info our InfoSec colleagues and they had some reservations on leading different subscription. But I think Mike and Chris, we can have a chat with them and see if we have to do this. I think now is the time and waste.
576072292608
Francisco Cachado   1:00:32
Hitesh.
576072292608
Sourabh Sardesai   1:00:35
Later on, we can't.
576072292608
Francisco Cachado   1:00:37
Yeah, yeah, like now is the now is the time, because now we only have EFF in dev, so it's like it's a quick thing to just restructure like the service connections, how the code is done now, to move to to a like a specific subscription level.
576072292608
Mike Agar   1:00:37
Yeah, good luck.
576072292608
Sourabh Sardesai   1:00:37
Move it back.
576072292608
Francisco Cachado   1:00:56
It will be easier to do now than later, yes.
576072292608
Sourabh Sardesai   1:01:01
So, so, so to summarize, it will be like dev subscription HR, dev subscription test, dev product subscription HR, and then...
576072292608
Francisco Cachado   1:01:09
No, no, it would be subscription, HR subscription, EFS subscription, sales.
576072292608
Sourabh Sardesai   1:01:15
But then again, how are we then we are then just limiting it to, so for productions production workloads, it has to be isolation isolation, right? If you are creating everything in in one subscription on dev test and prod, then we are putting dev and also production at risk.
576072292608
Francisco Cachado   1:01:33
If you want to have like that separation, we would need to create like...
576072292608
Vincent Rouet   1:01:33
Well...
576072292608
Francisco Cachado   1:01:36
Subscription EFF non-prod, subscription EFF prod. If you want to have like a completely different subscription between non-prod and prod.
576072292608
Sourabh Sardesai   1:01:47
So that's again a question then, because like you said, token limits are limited to subscription. So if I'm keeping one subscription as a bucket and dev and test and prod in the same thing, then if let's say my dev and testing is we are doing some tests and production has a high.
A volume, then the token limit server will impact the production workflows, which is, which is, which is more risky, I think.
576072292608
Francisco Cachado   1:02:09
And.
576072292608
Vincent Rouet   1:02:10
So.
Say that usually workloads would have two a dev test and a production subscription, so each workloads in this case, in your case, each domain would have two subs, right? And nothing goes very limited access to prod, obviously everything goes through CICD only.
576072292608
Francisco Cachado   1:02:18
Yeah.
Two, two or tomorrow.
Yes.
576072292608
Vincent Rouet   1:02:32
elevated permissions, privilege, you know, PIM access to productions, but otherwise developers. And then sometimes you also have sandbox subscriptions, right? Even before you go into the dev test, you might have the ad hoc sandbox where you just want to try things out for a couple of weeks.
they are ephemeral, less limited, disconnected from network and production data just to try things out. You might have that already.
576072292608
Francisco Cachado   1:02:52
Mhm.
576072292608
Sourabh Sardesai   1:03:04
Well, yeah, that's the thing, right? I think we need to talk to other colleagues, Mike.
576072292608
Francisco Cachado   1:03:05
Yeah.
576072292608
Vincent Rouet   1:03:08
They usually, yeah.
576072292608
Mike Agar   1:03:09
I think I think we need to know why we're doing these. So, what is what is the recommended thing?
You know what, what, what are we trying to, and and and why?
We're talking about splitting things out for subscriptions, but I'm still not quite clear why, right? Segregation, sure. Does it make things easier to manage or harder to manage? Does it mean we have more LLMs we're managing or, you know, why are we doing, what is kind of the proposal, I suppose, and why is that better than the alternative options?
576072292608
Francisco Cachado   1:03:34
I.
576072292608
Mike Agar   1:03:40
We can talk to InfoSec, I'm just...
576072292608
Vincent Rouet   1:03:41
Yeah.
576072292608
Mike Agar   1:03:43
Do they, do they care? Right? I feel like they're sort of, we should be presenting something to InfoSec and saying, this is how we're going to manage it. I'm also slightly worried, Sourabh. This is like fundamental architecture of development, isn't it? This is, it's not actually agent. This isn't anything to do with agents, actually, arguably.
576072292608
Francisco Cachado   1:03:50
In terms of...
576072292608
Sourabh Sardesai   1:03:54
Exactly, exactly, so a big, it's it's an entire.
576072292608
Francisco Cachado   1:03:57
Yeah, yeah, exactly. Yeah, this is not specific. Yeah, this is not specific for agents. And like in terms of work, to be honest, Mike, it will be kind of like already the similar work. Why? Because the InfoSec team now needs to create our resource group, it needs to create the service connectors, it needs to provision those same roles. So
576072292608
Mike Agar   1:04:14
Yeah.
576072292608
Francisco Cachado   1:04:17
If we are doing segregation at subscription level or at resource group level, it's the same effort for the infosec team. Now it's more if we want to fully segregate and have much more control between all the subscription.
576072292608
Sourabh Sardesai   1:04:31
And, and...
And you know what, we already have the legacy systems in is divided into, so for example, AIS layer, right, maximum AIS layer on all of this, it's still segregated under 2 subscriptions, non-prod and production, right? So how are we going to then use them with this?
Solve it, big change.
576072292608
Francisco Cachado   1:04:54
Yeah, that, yeah, all of that would need to be peered again with these ones if they are not peered yet to the entire tenant of mighty. If it's like subscription level peering, yeah, that would be like we would need to put.
576072292608
Vincent Rouet   1:04:54
Yep.
576072292608
Francisco Cachado   1:05:12
All over again, but I don't see.
576072292608
Vincent Rouet   1:05:14
Yeah, I mean, I remember before we started this program, we all agreed that it might be a big undertaking to change this, you know, the Microsoft Cloud Option Framework, this type of recommendations. And, you know, if it is going to delay too much, this is a separate thread. I think Poorna, she's leading on, she's having some conversation on this, right?
576072292608
Francisco Cachado   1:05:15
Gs.
576072292608
Mike Agar   1:05:15
Tew.
576072292608
Sourabh Sardesai   1:05:32
Yeah, the air lending something, yeah.
576072292608
Vincent Rouet   1:05:34
For the time being, you know, probably for this exercise, just use whatever is available today and work from that premise. So, yeah, 2 subscriptions and use results group isolation.
576072292608
Francisco Cachado   1:05:47
But, but I fully agree with you, I fully agree with you, Mike. We need like to like talk with the like Jordan. I don't know if if Peter is the correct person or not from the InfoSec side to understand their perspective on on this topic, if they, if...
576072292608
Sourabh Sardesai   1:06:02
Think, think, Veitch.
576072292608
Mike Agar   1:06:02
I think I think what we should try to do, Francisco, we can, is just say this is what we're proposing, right? It sounds like we've already got resource groups for these things, at least some of them. EFF, there's a resource group, so it's already there.
576072292608
Francisco Cachado   1:06:11
Yeah, yeah, yeah, we have, we have.
Yeah, and it's deployed, yes.
576072292608
Mike Agar   1:06:15
This bit at the bottom, are we doing it like this for every pillar and have three of them or 10 of them or however many pillars we have? Or are we saying that is a shared resource group across dev, a separate one for test? Are we saying it should be across both? Do we think that's right? Let me know, what is our proposal for this? And then based on that, and does it have failover, right? Do we need two of them? Maybe not down here, but maybe over here.
576072292608
Francisco Cachado   1:06:22
Mhm.
Mmh.
576072292608
Mike Agar   1:06:40
But this is the proposed architecture. And then that goes into KDD and that's what we send across to Pete and everyone else and just say, this is what we're proposing. And we've decided to do it because we don't want to mess up the existing, you know, that's part of the reasoning. It's this is how Mighty works today, changing it would be massive. It's nothing to do with AI. It's just how you manage code and environments.
576072292608
Vincent Rouet   1:06:56
Yeah.
576072292608
Francisco Cachado   1:06:59
Yeah, if we, if...
576072292608
Mike Agar   1:06:59
So, we're sticking to the existing pattern.
576072292608
Francisco Cachado   1:07:01
Yeah, if if we don't want like to change a lot of like and create like a huge burden on on refactoring the current the current mighty infrastructure, it's to follow the approach that you have now, and and then broad subscription, broad subscription, and we put all the resource groups inside.
576072292608
Mike Agar   1:07:19
Yep.
Yep.
576072292608
Francisco Cachado   1:07:21
That is like we already have the Terraform code working and so on. The question was here, it was like to understand if there was the need to change to a place where we have people subscription, not resource groups, subscriptions to handle all of this.
576072292608
Mike Agar   1:07:25
Yeah.
Yeah. And if there is, then I guess my question is, who needs it? Why? You know, are you asking for it, Francisco? Because you're saying the best practise was we do it is it's much better to manage it in a new subscription because it, or is it InfoSec that we think might ask for this or is it, you know, who's asked? Why are we changing it?
Because if there's no, you know, thinking pros and cons, right? The con is it's going to affect everything. The pro is...
576072292608
Francisco Cachado   1:07:58
Yeah.
Mhm.
576072292608
Mike Agar   1:08:03
I don't know what the pro is.
576072292608
Francisco Cachado   1:08:03
The pro is like, yeah, is like the the segregation and like, if you have in mind the least privilege approach, where do you like, because now is like, if you do like, because I already did that exercise, if you go to like, for example, to our like to the resource group we have for the for the for the EFF, you'll see that you have a lot of
rules. So everyone that is inside of the subscription, even that is not part of the FF, will have those rules inside. So if you look into, if you look into a least privilege approach, you say, okay, so it's better to have like a subscription only specific.
576072292608
Mike Agar   1:08:34
Sure.
But that is...
Sure.
Sure, but that.
576072292608
Francisco Cachado   1:08:46
If it's something that is already agreed inside of MakingItHappen, let's move with the current system that you have in place, and that's the drawing that you have on your screen. You are not sharing, but was the drawing that you were that you were sharing.
576072292608
Mike Agar   1:08:51
Yeah.
Yep.
Oh yeah, so I think it's how we work today. InfoSec must have agreed with it because it's already working. We can have a 30 second chat with Jordan and the next stand up, right, and just say, is there any problem?
576072292608
Francisco Cachado   1:09:02
Yep.
Yeah, exactly.
Yeah, and cheque with him. Yeah, exactly.
576072292608
Mike Agar   1:09:12
But this is how it works and it's nothing to do with AI, right? It's exactly the same as you were to create a new resource group to go off and build the next project. So.
576072292608
Francisco Cachado   1:09:15
Yeah, this is not.
Yeah, this is nothing, nothing. This is not really the two ai. This is like the way mighty decided to move forward with that with that structure.
576072292608
Mike Agar   1:09:19
I, I just...
Yeah.
So, I, I, yeah, so I don't, I don't think we need to change it. The question we need to work out is is this bit.
Maybe these domains, right? If we really think the domains are a good idea, you know, should we just be having one mega resource group for dev or lots? You know, I don't quite understand the reason why we split it into these, what I think are basically arbitrary domains, right? I know we've got the Prio project with domains in it, but they're just random work streams that someone's come up with for a project.
576072292608
Francisco Cachado   1:09:52
Mhm.
576072292608
Mike Agar   1:09:55
Do they make sense logically? Why have we divided it this way? Is it for billing? That would make sense, right? If it's purely for reporting billing, that might be an answer in itself. But I just want to make sure we're clear why we've divided it like that.
576072292608
Francisco Cachado   1:10:07
Between what? EFF HR?
576072292608
Sourabh Sardesai   1:10:08
And, and, and that's why, and that's why Mike, what what I've done is I have not given a name of the resource group as EFF as such, I've given it as a technical services dev version, so essentially anything related to technical services, yeah, my business unit.
576072292608
Mike Agar   1:10:08
And then.
by business unit.
576072292608
Francisco Cachado   1:10:23
But then, okay, but sort of, but then inside, we then to cheque what will be the name because technical services, it's too big for the restriction that Azure has on these resources. So we cannot have it like so big.
576072292608
Sourabh Sardesai   1:10:30
Yeah.
Exactly, so, so the...
So, yeah, so the resource group is technical services, but the resources created within it can have EFF as a, you know, as a, yeah, so that just to make sure that, and we also use tags, you know, we can also use, we also using the tags to differentiate, yeah.
576072292608
Francisco Cachado   1:10:42
Yeah, it's the FFPS.
Okay.
No, no, yeah, we have like everything is set, everything else on Mike for that, everything is tagged, so if if you go to cost, you can like philtre by tags, so you have you can search only for like compute inside EFF or compute inside of.
576072292608
Mike Agar   1:11:04
So, so.
So why do we not just have one?
576072292608
Francisco Cachado   1:11:10
One, what?
576072292608
Mike Agar   1:11:12
One Resource Group for Dev.
576072292608
Francisco Cachado   1:11:15
No, no, that's it, like that, that would be like, I, I would not say that.
576072292608
Sourabh Sardesai   1:11:16
No, yeah, that so we won't be able to.
That will be so.
576072292608
Francisco Cachado   1:11:21
This is not like the the the best approach, like we we should have, yeah, we need to we need to have.
576072292608
Sourabh Sardesai   1:11:24
Access.
There'll be a problem with access.
576072292608
Francisco Cachado   1:11:29
Yeah, we need to have like everything separated, like everything by work stream or slash domain.
576072292608
Mike Agar   1:11:29
Bye.
Yeah.
576072292608
Sourabh Sardesai   1:11:34
Yeah.
Yeah.
576072292608
Francisco Cachado   1:11:43
Because we need to upset.
Yeah.
Mhm.
Nope.
576072292608
Mike Agar   1:11:52
Some.
Reasoned decisions.
576072292608
Francisco Cachado   1:11:54
Because, if we do that, what can end up is, for example, we will have like 3 key vaults in the same subscription, the same managed identity will have access to all of those key vaults, and if one if something is like compromised.
You have the entire thing compromised.
576072292608
Mike Agar   1:12:16
I get that, but...
576072292608
Francisco Cachado   1:12:16
So, you don't have any installation?
576072292608
Mike Agar   1:12:19
I get that, but it's describing why it's at this level of granularity, not either lower or higher. Tech services is quite a big, that's a big area, right? That's the, that's like half the business. It would mean you have business services.
576072292608
Vincent Rouet   1:12:30
Mm.
576072292608
Francisco Cachado   1:12:30
No, but like this, this, but yeah, but this name was like this came with, but technical services is for, it's where we're gonna put like all the EFF domain work.
576072292608
Mike Agar   1:12:41
Yeah.
576072292608
Francisco Cachado   1:12:42
And then we'll have a I have to retire.
576072292608
Vincent Rouet   1:12:44
Okay.
576072292608
Mike Agar   1:12:45
Vincent, you don't have to stick for this. I think we're getting into deep mighty here, but it's up to you.
576072292608
Francisco Cachado   1:12:50
Yeah.
576072292608
Vincent Rouet   1:12:51
No, but I think it's a good point, Mike. It's either...
divisions, but they can be completely unequal, right? There's some bigger ones. So the other way is sometimes to group by some sort of level security tier, right? Tier one, tier 2, tier 3 type of applications, where you group them by level of SLA, level of security requirements.
Yeah.
576072292608
Francisco Cachado   1:13:22
Like, when we start to align these, it was like we would separate in resource groups, so meant like when we like when we start to the to to design it to OK, we have two subscriptions. Instead of each subscription, we have multiple resource groups, one per environment slash the the domain.
576072292608
Vincent Rouet   1:13:22
Yeah.
576072292608
Mike Agar   1:13:41
Yeah, and look, I'm challenging because I have to, right? But it all makes sense, but...
576072292608
Francisco Cachado   1:13:42
But.
Yeah, no, no.
576072292608
Mike Agar   1:13:48
We got to remember Prio is a project. The work streams in Prio are completely arbitrary and transitory.
And therefore it cannot be in the KDD. We divided this up into groups that match the pre-o project structure. That cannot be the reason.
So why did we divide it up this way? And we either need to come up with a logical reason why EFF is a sensible group, HR is a sensible group, sales is a sensible, you know, we have any good reasons or we need to rethink why we've done it.
576072292608
Francisco Cachado   1:14:14
Because it's like, because it's like each domain of the project, like that work stream, so those those were the names we came with for that for that, so if if tomorrow like we want to to start having the, for example, support team support team office like.
576072292608
Mike Agar   1:14:20
Yeah, but that...
576072292608
Emma Sun   1:14:22
Yes.
576072292608
Francisco Cachado   1:14:34
SDH will create like an SDH vertical box here alongside HR and the FF.
576072292608
Mike Agar   1:14:44
But it, but it, it, whatever we do, it can't be project back that logic, Francisco, can't work right? We can't build our infrastructure around a project.
576072292608
Emma Sun   1:14:53
Okay, sorry, guys.
576072292608
Francisco Cachado   1:14:54
No, and that, and that will be real that, like, my, the idea is, like, I'm not, I'm not saying like project names, I'm talking about solution naming.
576072292608
Emma Sun   1:14:57
Ha.
So guys, we're 15 minutes over. I think this is a good discussion, but it sounds like Francisco Sourabh like we need to regroup and like think through this and then we can come back with a good reasoning on like why, right? Because that has been one of like my has been asking you the past 15 minutes. It's like why, right? We need a really.
576072292608
Sourabh Sardesai   1:15:13
Yeah.
576072292608
Francisco Cachado   1:15:16
Age.
576072292608
Mike Agar   1:15:23
Ha.
576072292608
Emma Sun   1:15:25
Strong evidence, I mean, if there's no need, then we don't do it, like we're not.
576072292608
Sourabh Sardesai   1:15:25
Yeah, yeah, yeah.
Yeah, yeah. Cool.
576072292608
Emma Sun   1:15:31
pushing it, it must be segregate, but anyways, yeah, let's regroup. Okay.
576072292608
Sourabh Sardesai   1:15:33
Yeah.
576072292608
Mike Agar   1:15:35
Yeah, alright, cool.
576072292608
Sourabh Sardesai   1:15:36
Yeah, well, good discussion, good call. Thank you so much.
576072292608
Emma Sun   1:15:39
Thank you so much.
576072292608
Mike Agar   1:15:40
Yes, I'll try to get minutes out of this, so I'll see how I...
576072292608
Francisco Cachado   1:15:43
Thank you, everyone.
576072292608
Mike Agar   1:15:43
It might be tough.
576072292608
Emma Sun   1:15:45
Thank you so much, Maya. I like your manner. They're really helpful.
576072292608
Mike Agar   1:15:48
Good. Right.
576072292608
Sourabh Sardesai   1:15:48
But.
576072292608
Emma Sun   1:15:49
Thanks for keeping us on track. Cool. All right.
576072292608
Francisco Cachado   1:15:51
I.
576072292608
Mike Agar   1:15:51
Well, not doing a great job at that given it's quarter past, but thanks everyone. See you later. Thank you.
576072292608
Sourabh Sardesai   1:15:51
Well, thank you.
576072292608
Emma Sun   1:15:52
Coco.
576072292608
Vincent Rouet   1:15:53
Thank you.
576072292608
Sourabh Sardesai   1:15:54
Cheers guys. Bye, bye, bye, bye.
576072292608
Emma Sun   1:15:54
Thanks, Damien. Yeah. All right.
576072292608
Francisco Cachado   1:15:55
Thanks.
621792274320
Mike Agar stopped transcription

