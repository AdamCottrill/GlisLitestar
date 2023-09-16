 SELECT
  [PRJ_CD],
  [SAM],
  [EFF],
  [SPC],
  [GRP],
  [FISH],
  [FISH_TAG_ID],
  [TAGID],
  [TAGDOC],
  [TAGSTAT],
  [CWTSEQ],
  [COMMENT_TAG]
 FROM [FN125_Tags]
  where
 [prj_cd]=? and
 [sam]=? and
 [eff]=? and
 [spc]=? and
 [grp]=? and
 [fish]=? and
 [fish_tag_id] = ?
