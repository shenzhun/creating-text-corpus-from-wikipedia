import re
import sys

#=========================================================================
#
# Wiki Markup Grammar
# Redirect   <text>#REDIRECT .*? </text>
# Template   {{" [ "msg:" | "msgnw:" ] PageName { "|" [ ParameterName "=" AnyText | AnyText ] } "}}
# Media      [[(File|Media|Image|Category):.*]]
# NoWiki     "<nowiki />" | "<nowiki>" ( InlineText | BlockText ) "</nowiki>" ;
# Parameter  "{{{" ParameterName { Parameter } [ "|" { AnyText | Parameter } ] "}}}" ;
# Comment    "<!--" InlineText "-->" | "<!--" BlockText "//-->" ;
# Ref        ref name=.*;?
# Entity     &lt;|ref&gt;|/ref&gt;|&quot|&gt|&amp       
# List       * | #
# Font       '', ''', '''' 
# Heading    ==, ===, =====
# Link       [http:... ]
#
#===========================================================================

f1 = open(sys.argv[1], 'rb').read()
list = re.findall('<text.*?>(.*?)</text>', f1, flags=re.S)
for content in list:

    # remove redirect text content
    txt = re.sub('^#REDIRECT.*$', '', content)
    
    # discard tags of Wiki
    discard_dbracket = re.sub('\{\{.*?\}\}', '', txt, flags=re.S)
    discard_bracket = re.sub('\{\|.*?\|\}', '', discard_dbracket, flags=re.S)
    
    discard_font = re.sub("'{2,5}", '', discard_bracket)
    discard_media = re.sub('\[\[(Category|Image|Media|File):.*\]\]', '', discard_font)
    discard_link = re.sub('\[\[|\]\]', '', discard_media)
    discard_http = re.sub('\[http://.*\]', '', discard_link)
    discard_heading = re.sub('={2,5}', '', discard_http)
    discard_html_entity = re.sub(r'&lt;|ref&gt;|/ref&gt;|&quot|&gt|&amp', '', discard_heading)
    discard_ref = re.sub('ref name=.*;?', '', discard_html_entity)
    discard_list = re.sub('[*|#]\s.*\n', '', discard_ref)
    discard_blank = re.sub('(\n)+', '\n', discard_list)
    with open(sys.argv[1]+'.xmltext', 'a') as fw:
	    fw.write(discard_blank)

