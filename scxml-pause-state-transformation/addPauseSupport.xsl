<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
	xmlns:s="http://www.w3.org/2005/07/scxml"
	xmlns="http://www.w3.org/2005/07/scxml"
	xmlns:c="http://commons.apache.org/scxml-js"
	version="1.0">
	<xsl:output method="xml"/>

	<xsl:param name="pauseEventName" select="'$PAUSE'"/> 
	<xsl:param name="unpauseEventName" select="'$UNPAUSE'"/> 

	<!-- identity transform -->
	<xsl:template match="@*|node()">
		<xsl:copy>
			<xsl:apply-templates select="@*|node()"/>
		</xsl:copy>
	</xsl:template>


	<xsl:template match="/s:scxml">

	
		<xsl:copy>
			<!--<xsl:apply-templates select="@*[not(self::initial)]"/>-->
			<xsl:apply-templates select="@profile"/>
			<xsl:apply-templates select="@version"/>

			<!-- get the top-level initial state -->
			<xsl:variable name="originalInitialState" select="@initial | s:initial/s:transition/@target"/>

			<xsl:variable name="newCompositeStateId" select="concat('composite_',generate-id())"/>
			<xsl:variable name="newHistoryStateId" select="concat('history_',generate-id())"/>
			<xsl:variable name="newPauseStateId" select="concat('pause_state_',generate-id())"/>

			<initial>
				<transition target="{$newCompositeStateId}"/>
			</initial>

			<!-- new top-level composite state, with deep history -->
			<state id="{$newCompositeStateId}">
				<initial>
					<transition target="{$newHistoryStateId}"/>
				</initial>

				<history type="deep" id="{$newHistoryStateId}">
					<transition target="{$originalInitialState}"/>
				</history>

				<transition target="{$newPauseStateId}" event="{$pauseEventName}"/>

				<xsl:apply-templates select="*[not(self::s:initial)] | text()"/>
			</state>

			<!-- new pause state -->
			<state id="{$newPauseStateId}">
				<transition target="{$newCompositeStateId}" event="{$unpauseEventName}"/>
			</state>
			
		</xsl:copy>
	</xsl:template>
</xsl:stylesheet>
