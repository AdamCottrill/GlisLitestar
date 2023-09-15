SELECT
     [PRJ_CD],
     [SAM],
     [EFF],
     [SPC],
     [GRP],
     [FISH],
     [AGEID],
     [PREFERRED],
     [AGEA],
     [AGEMT],
     [EDGE],
     [CONF],
     [NCA],
     [AGESTRM],
     [AGELAKE],
     [SPAWNCHKCNT],
     [AGE_FAIL],
     [COMMENT7]
FROM [FN127] where
    [prj_cd]=? and
    [sam]=? and
    [eff]=? and
    [spc]=? and
    [grp]=? and
    [fish]=? and
    [ageid]=?
