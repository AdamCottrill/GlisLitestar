SELECT
  [PRJ_CD],
  [SAM],
  [EFF],
  [SPC],
  [GRP],
  [FISH],
  [LAMID],
  [XLAM],
  [LAMIJC_TYPE],
  [LAMIJC_SIZE],
  [COMMENT_LAM]
FROM [FN125_Lamprey]
 where
  [prj_cd]=? and
  [sam]=? and
  [eff]=? and
  [spc]=? and
  [grp]=? and
  [fish]=? and
  [lamid] = ?
