# Setting Up Your Second Brain Folder Structure

![image](./images/banner.png)

---

Before we start, let’s talk about why we are doing this.

Right now, a lot of people are talking about the Karpathy Wiki idea. The main idea is simple: instead of keeping knowledge only in your head, you store it in a clear system that you can reuse later. We are going to build something similar for ourselves. We will call it a Second Brain.

Why does this matter? Because when you work with data, tools, and AI, you need a place to keep everything organized. If your files are scattered everywhere, it becomes hard to find things later. A Second Brain helps you keep your work clean, simple, and easy to follow.

In this lesson, we will set up the folder structure that will hold our data, our instructions, and our wiki. We will also learn how tools like Snowflake, MCP servers, Composio, and Apify fit into the process.

Before we begin, you have two choices:

- download the folder template we prepared for you
- create your own structure from scratch

We will start with the template so you can move faster and focus on learning.

---

## What We Are Building

We are creating a folder called `Second-Brain`.

Think of it like this: your brain can think, but it cannot hold everything forever. A Second Brain is a place outside your mind where you keep the work you are doing. It can hold raw data, notes, useful files, and the instructions that help Claude understand your work.

For this course, we will use Maven as our example. Maven runs courses like the AI PM Bootcamp and GenAI PM course. It also shares content on LinkedIn and YouTube. Our job is to:

- bring in raw data from LinkedIn, YouTube, and Zoom
- send that data into Snowflake
- build a wiki that Claude can read and use when we ask questions

The `wiki/` folder is the main part of this system. It is where we keep our organized knowledge so Claude can use it when needed.

---

## Step 1: Download the Template

You can download the Second Brain template we prepared for this course:

> **[Download Second Brain Template](https://pragyaallc-my.sharepoint.com/:u:/g/personal/sachin_parmar_legalgraph_ai/IQBdu9h0h8gySLzjtxWGDBCrAa6utw4kKY1Ycf0U304Z4CA?e=XXaBFR)**

This gives you the folder structure and example files so you do not have to build everything from zero.

---

## The Full Structure

This is what the folder looks like:

```text
Second-Brain/
├── raw/
│   ├── LinkedIn-ads.json
│   ├── LinkedIn-campaign.json
│   └── YouTube-channel.json
├── skill/
│   ├── push-data-to-snowflake.md
│   ├── build-wiki.md
│   └── build-wbr.md
├── wiki/
│   ├── campaigns/
│   │   ├── README.md
│   │   ├── linkedin-ads/
│   │   ├── linkedin-campaign/
│   │   └── youtube/
│   └── courses/
│       ├── course-bootcamp.md
│       └── course-genaipm.md
└── Archive/
```

Each folder has a job:

- `raw/` holds the original files we collect from tools like LinkedIn and YouTube
- `skill/` holds the instruction files that guide Claude
- `wiki/` holds the organized knowledge that Claude can read
- `Archive/` is where files go after they have been used

---

## Why This Structure Matters

A good folder structure makes work easier.

When everything has a home, you spend less time searching and more time building. You also make it easier for others to understand your work. This is how real teams work too. They do not leave things in random places.

This structure helps us keep our work clear from the beginning.

---

## What You Have Learned

By now, you should understand:

- what a Second Brain is
- why we are building one
- what each folder in the structure is for
- how data moves from tools into Snowflake and then into the wiki

---

## What’s Next

**[Lesson 0.2 → Create Your Composio Account](../0.2-creating-composioaccount/readme.md)**

In the next lesson, we will create our Composio account. Composio helps connect Claude with tools like YouTube, LinkedIn, and Snowflake.

---