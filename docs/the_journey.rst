The Journey to the Extraction of Fields
=======================================

The problem
-----------

*This is the meat of the project. This is the most important part!*

So basically the idea is, How do we identify and extract each question and it's
related answer field (e.g. Text box, Checkbox, Radio buttons, Drop downs, etc)?

The challenge
-------------

The most difficult challenge in identifying individual parts of the web forms is that
each stupid HR website has its own framework/structure to build the form. Since their
content is highly dynamic, no two HR website use the same pattern. Especially, I've seen weak to none
adherence to the standard HTML form structure.

The solutions
-------------

This is a tough nut to crack!

Since starting the project, up until now, I've though about and researched different
solutions:

1. Rule Based Extraction:

This is basically the way to tell selenium what to extract from a form using IF
... THENs. This method relies on pseudo-unique features of each forms. The
extensibility of this method is extremely limited.

I have already made an example of such approach in my code.

2. Computer Vision:

Using image recognition techniques to find the elements of a web page.

This approach needs you to transmit the page data as picture format. Obviously
computer vision looks like the closest approach to *Natural* human perception of forms.

However, there are some pro

3. AI/NLP/ML
   


   3.1. LLMs

   OpenAI and models like **Phind** are promising

   There's also a whole list of local LLMs. More info at `This Subreddit <https://www.reddit.com/r/LocalLLaMA/>`_

   3.2. Extractnet

   This is the main subject of this project. It's forked from `The original project <https://github.com/currentslab/extractnet>`_.
   However, it's outdated and I'll probably change it.

   3.3. Trafilatura

   This is a very interesting `python library <https://trafilatura.readthedocs.io/>`_ to extract main contents and remove boilerplates from a page.

   3.4. Retrieval-Augmented Generation (RAG):

   This can't be directly applied to web scraping; however, it's a family of methods designed 
   to retrieve the body of knowledge from scanned documents (with tables, figures, etc) and
   add them to a LLM. Later we can ask the LLM questions related to that body of knowledge.

   More Info:

   `Retrieval-Augmented Generation (RAG) from basics to advanced <https://medium.com/@tejpal.abhyuday/retrieval-augmented-generation-rag-from-basics-to-advanced-a2b068fd576c>`_

   `The RAG Engineer's Guide to Document Parsing <https://www.reddit.com/r/LangChain/comments/1ef12q6/the_rag_engineers_guide_to_document_parsing/>`_

   *Note*: Gemini has a similar feature that's researching the open web about a topic and gathering the
   required info....


Scientific Background
---------------------

For now, I haven't done much focus on the more scientific knowledge and papers. 
I believe that the technology has sufficiently reached maturity that right now some 
tools and public / paid services are available.

However, some general scientific background knowledge is good to gain a keyword-level understanding
of the domain.

So I'll list some related articles here:

*Note*: If the links don't work, I have them in my drive.

1. **Boilerplate Detection Using Shallow Text Features** (`ref <https://www.researchgate.net/publication/221519989_Boilerplate_Detection_Using_Shallow_Text_Features>`_)

   This one is the backbone of the Extractnet project. 
   It is highly cited (694). However, it's old (2010) and Im not sure how useful it could be.
   Still it was good for keyword searching so far!