
SELECT [PRJ_CD],
             [SAM],
             [EFF],
             [SPC],
             [GRP],
             [CATCNT],
             [BIOCNT],
             [CATWT],
             [SUBCNT],
             [SUBWT],
             [COMMENT3]
        FROM FN123 where prj_cd=? and sam=? and eff=? and spc=? and grp=?
