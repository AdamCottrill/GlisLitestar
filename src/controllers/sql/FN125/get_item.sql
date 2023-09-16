SELECT
 [PRJ_CD],
 [SAM],
 [EFF],
 [SPC],
 [GRP],
 [FISH],
 [FLEN],
 [TLEN],
 [GIRTH],
 [RWT],
 [EVISWT],
 [SEX],
 [MAT],
 [GON],
 [GONWT],
 [CLIPC],
 [CLIPA],
 [NODC],
 [NODA],
 [TISSUE],
 [AGEST],
 [FATE],
 [FDSAM],
 [STOM_CONTENTS_WT],
 [COMMENT5]
FROM [FN125]
 where
[prj_cd]=? and
[sam]=? and
[eff]=? and
[spc]=? and
[grp]=? and
[fish]=?
