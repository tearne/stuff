#!/usr/bin/env bash
R --no-save << EOF
install.packages(
	c(
		"ggplot2",
		"reshape2",
		"jsonlite",
		"plyr",
		"GGally"
	),
	dependencies=T,
	repos="http://cran.ma.imperial.ac.uk"
)
quit("no")
EOF