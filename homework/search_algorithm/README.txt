 This data set is made available under a Creative Commons License:
  http://creativecommons.org/licenses/by/3.0/

  Attribution 3.0 Unported (CC BY 3.0) Human-Readable Summary
  ===========================================================

  You are free:
   - to Share -- to copy, distribute and transmit the work;
    - to Remix -- to adapt the work;
    and to make commercial use of the work.


    Under the following conditions:

    * Attribution -- You must attribute the work in the manner specified
    by the author or licensor (but not in any way that suggests that
    they endorse you or your use of the work).


    With the understanding that:

    * Waiver -- Any of the above conditions can be waived if you get
    permission from the copyright holder.

    * Public Domain -- Where the work or any of its elements is in
    the public domain under applicable law, the status is in no way
    affected by the license.

    * Other Rights -- In no way are any of the following rights
    affected by the license:

    - Your fair dealing or fair use rights, or other applicable
    copyright exceptions and limitations;

    - The author's moral rights;

    - Rights other persons may have either in the work itself or
    in how the work is used, such as publicity or privacy rights.

    * Notice -- For any reuse or distribution, you must make clear
    to others the license terms of this work.  The best way to do
    this is with a link to this web page:
    http://creativecommons.org/licenses/by/3.0/


 Introduction
 ============

 The Wikipedia links (WikiLinks) data consists of web pages that
 contain at least one hyperlink that points to English Wikipedia. 
 The data set was obtained by iterating over Google's web index.
 We treat each page on Wikipedia as representing an entity (or concept 
 or idea), and the anchor text as a mention of that entity. We have
 done some filtering to ensure that the anchor text can be a mention
 of the entity that it links to (e.g., we remove anchors such as
 "click here").

 Content
 =======

 This dataset is accompanied by the following tech report:

 https://web.cs.umass.edu/publication/docs/2012/UM-CS-2012-015.pdf

 Please cite the above report if you use this data.

 The dataset is divided over 10 gzipped text files
 data-0000[0-9]-of-00010.gz. For example:

 zcat data-00001-of-00010.gz | head 

 gives:

 URL	ftp://121.244.82.26/BENarkhede/ben-official/Utilizing%20Six%20Sigma%20for%20Defect%20Reductions-%20A%20Case%20Study.doc
 MENTION	quality control	49584	http://en.wikipedia.org/wiki/Quality_control
 TOKEN	right	14911
 TOKEN	smarter	14944
 TOKEN	driven	9151
 TOKEN	defines	81657
 TOKEN	laboratory	34360
 TOKEN	workshop	41603
 TOKEN	savings	89906
 TOKEN	Korean	96665

 Each file is in the following format:

 -------

 URL\t<url>\n
 MENTION\t<mention>\t<byte_offset>\t<target_url>\n
 MENTION\t<mention>\t<byte_offset>\t<target_url>\n
 MENTION\t<mention>\t<byte_offset>\t<target_url>\n
 ...
 TOKEN\t<token>\t<byte_offset>\n
 TOKEN\t<token>\t<byte_offset>\n
 TOKEN\t<token>\t<byte_offset>\n
 ...
 \n\n
 URL\t<url>\n
 ...

  -------

 where each web-page is identified by its url (annotated by
 "URL"). For every  mention(denoted by "MENTION"), we provide the
 actual mention string, the byte offset of the mention from the start
 of the page and the target url all separated by a tab. It is
 possible (and in many cases very likely) that the contents of a
 web-page may change over time. The dataset also contains information
 about the top 10 least frequent tokens on that page at the time it
 was crawled. These line started with a "TOKEN" and contain the string
 of the token and the byte offset from the start of the page. These
 token strings can be used as fingerprints to verify if the page used
 to generate the data has changed. Finally, pages are separated from
 each other by two blank lines. 

 Some approximate counts:
 ========================

 Number of Documents: 13 million
 Number of mentions: 59 million

 Please note that this dataset was created automatically from the web
 and therefore contains some amount of noise.

 Enjoy!

 Amar Subramanya (asubram@google.com)
 Fernando Pereira (pereira@google.com)
 Sameer Singh (sameer@cs.umass.edu)
 Andrew McCallum (mccallum@cs.umass.edu)
