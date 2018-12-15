<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <head>
        <title>Co-auteurs</title>
      </head>
      <body>
        <h1>Extrait concernant <xsl:value-of select="extract/name"/> </h1>
        <h2>Coauteurs</h2>
        <p> <xsl:value-of select="extract/name"/> a écrit avec
          <xsl:choose>
            <xsl:when test="count(extract/coauthors/author) &gt; 1">
              <xsl:value-of select="count(extract/coauthors/author)"/> personnes:

              <ul>
                <xsl:for-each select="//extract/coauthors/author[not(preceding::author/. = .)]">
                    <xsl:sort select="text()"/> <li> <xsl:value-of select="text()"/> </li>
                </xsl:for-each>
              </ul>

            </xsl:when>
            <xsl:when test="count(extract/coauthors/author)=0">
              personne.
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="count(extract/coauthors/author)"/> personne:

              <ul>
                <xsl:for-each select="extract/coauthors/author">
                  <li> <xsl:value-of select="text()"/> </li>
                </xsl:for-each>
              </ul>

            </xsl:otherwise>
          </xsl:choose>
        </p>

        <h2>Articles</h2>
        <p>
          <xsl:value-of select="extract/name" />
          <xsl:choose>
            <xsl:when test="count(extract/article)=0">
              n'a pas écrit d'articles.
            </xsl:when>
            <xsl:when test="count(extract/article) &gt; 1">
              a écrit <xsl:value-of select="count(extract/article)"/> articles:

              <ul>
                <xsl:for-each select="extract/article">
                  <xsl:sort select="year"/>  <li> <xsl:value-of select="title"/> </li>
                </xsl:for-each>
              </ul>

            </xsl:when>
            <xsl:otherwise>
              a écrit <xsl:value-of select="count(extract/article)"/> article:

              <ul>
                <xsl:for-each select="extract/article">
                  <li> <xsl:value-of select="title"/> </li>
                </xsl:for-each>
              </ul>

            </xsl:otherwise>
          </xsl:choose>

        </p>

        <h2>InProceedings</h2>
        <p>

          <xsl:value-of select="extract/name" />
          <xsl:choose>
            <xsl:when test="count(extract/inproceedings)=0">
              n'a pas écrit d'articles de type inproceedings.
            </xsl:when>
            <xsl:when test="count(extract/inproceedings) &gt; 1">
              a écrit <xsl:value-of select="count(extract/inproceedings)"/> articles de type inproceedings:

              <ul>
                <xsl:for-each select="extract/inproceedings">
                  <li> <xsl:value-of select="title"/> </li>
                </xsl:for-each>
              </ul>

            </xsl:when>
            <xsl:otherwise>
              a écrit <xsl:value-of select="count(extract/inproceedings)"/> article de type inproceedings:

              <ul>
                <xsl:for-each select="extract/inproceedings">
                  <li> <xsl:value-of select="title"/> </li>
                </xsl:for-each>
              </ul>

            </xsl:otherwise>
          </xsl:choose>

        </p>

        <h3>Statistiques sur les articles</h3>

        <ul>
          <xsl:for-each select="//extract/article/year">
            <xsl:sort select="current()"/>
            <xsl:variable name="currentYear" select="current()"/>
            <li>
                <xsl:choose>
                  <xsl:when test="count(//article[year=$currentYear]) &gt; 1">
                    <xsl:value-of select="//name"/> a ecrit <xsl:value-of select="count(//article[year=$currentYear])"/>
                    articles en <xsl:value-of select="$currentYear"/>
                  </xsl:when>
                  <xsl:otherwise>
                    <xsl:value-of select="//name"/> a ecrit <xsl:value-of select="count(//article[year=$currentYear])"/>
                    article en <xsl:value-of select="$currentYear"/>
                  </xsl:otherwise>
                </xsl:choose>
            </li>
          </xsl:for-each>
        </ul>

      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
