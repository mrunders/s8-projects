<?xml version="1.0" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output method="html" encoding="latin-1"/>
	<xsl:template match="recette">
		<html>
			<body>
				<h1><xsl:value-of select="titre"/></h1>
				<xsl:apply-templates />
			</body>
		</html>
	</xsl:template>
	
	<xsl:template match="nb-personnes">
		<p> Pour un nombre de personnes de: <xsl:apply-templates /></p>
	</xsl:template>
	
	<xsl:template match="tps-preparation">
		<p> Temps de préparation: <xsl:apply-templates /></p>
	</xsl:template>
	
	<xsl:template match="tps-cuisson">
		<p> Temps de cuisson: <xsl:apply-templates /></p>
	</xsl:template>
	
	<xsl:template match="difficulte">
		<p> Niveau:  <xsl:value-of select="@niveau" /></p>
	</xsl:template>
	
	<xsl:template match="ingredients">
		<h4>Ingrédients</h4>
		<ul>
		<xsl:for-each select="ingredient">
			<li>
			<xsl:value-of select="nom" />
				<xsl:if test="qte">
				<xsl:text>, </xsl:text>
				<xsl:value-of select="qte" />
				<xsl:text> </xsl:text>
				<xsl:value-of select="qte/@unite" />	
				</xsl:if>
			</li>
		</xsl:for-each>
		</ul>
	</xsl:template>
	
	<xsl:template match="preparation">
		<h3>Préparation</h3>
		<ol>
		<xsl:for-each select="phase">
			<li>
			<xsl:apply-templates />
			</li>
		</xsl:for-each>
		</ol>
	</xsl:template>

</xsl:stylesheet>
