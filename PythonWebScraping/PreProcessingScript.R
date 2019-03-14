###data preprocessing


df <- read.csv("C:/Users/John/Documents/GitHub/RugbyStats/testpage.csv")

###data tends to look good, other than some strange positions
df$position <- gsub("\\(", "", df$position)
df$position <- gsub("\\)", "", df$position)

unique.positions <- unique(df$position)
print(unique.positions)

### want to treat BP, R, UB somehow
### first guesses as to what these mean...
### BR = back row. we can likely set these to flanker (F) as a close approximation
### R = reserve. unless there is significant scoring here, likely get rid of
### UB = utility back. unless there is significant scoring here, likely get rid of

length(which(df$position == "BR" & df$points != 0))
### there's only 4 nonzero entries. going to assign these to flanker 
df$position[df$position == "BR"] <- "F"

length(which(df$position == "R" & df$points != 0))
### there's 31 nonzero point entries here, compared to 27,000 total entries
### i can likely get rid of these without significantly changing results
df <- df[-which(df$position == "R"),]

length(which(df$position == "UB" & df$points != 0))
### there's 1 nonzero point entries here, compared to 27,000 total entries
### i can likely get rid of these without significantly changing results
df <- df[-which(df$position == "UB"),]

### check on the points column. this one seems to be weird...
print(unique(df$points))

### take a look into the ones with G's... don't really have an explanation 
df[grep("G", df$points),]
length(df[grep("G", df$points),])

### only 10 entries... i can get rid of these without significantly affecting analysis

df <- df[-grep("G", df$points),]
print(unique(df$points))

df$points <- as.numeric(as.character(df$points))

### get rid of all entries that are zero- this doesn't add anything and will just 
### make tableau calculations slower

df <- df[-which(df$points == 0),]
# df$points <- as.numeric(df$points)
summary(df)

countries <- read.csv("C:/Users/John/Documents/GitHub/RugbyStats/countries.csv")

### add in the tiers for both country, opposition
country.matching <- match(df$country, countries$Country_abbrev)
opposition.matching <- match(df$opposition, countries$Country_name)
df$country_tier <- countries$Country_tier[country.matching]
df$opposition_tier <- countries$Country_tier[opposition.matching]

### check any NA's that are left over. They are likely tier 3, but could be typo...

unique(df[is.na(df$country_tier), "country"])
### Lions, Korea, HK, PI, Arab, Cooks
### give Lions their own category. could be fun to compare them to tier 1 nations
df$country_tier[df$country == "Lions"] <- "Lions"

### the rest of these are tier 3

df$country_tier[is.na(df$country_tier)] <- 3

unique(df[is.na(df$opposition_tier), "opposition"])

### there's a lot of national developmental teams (NZ Maori, Argentina XV, etc..)
### for consistency, we will delete these
emerging.natl.teams <- unique(df[is.na(df$opposition_tier), "opposition"])[c(c(10:15),c(17:26))]


for (i in 1:length(emerging.natl.teams)){
  rows.to.del <- which(df$opposition == emerging.natl.teams[i])
  df <- df[-rows.to.del,]
}

### USA is tier 2
df$opposition_tier[df$opposition == "USA"] <- 2

### make separate tier barbarians/lions
df$opposition_tier[df$opposition == "Barbarians" | df$opposition == "Lions"] <- "Lions/Barb"

### remaining are all tier 3
df$opposition_tier[is.na(df$opposition_tier)] <- 3

### let's make columns for the amount of points scored per each type

df$points_tries <- df$tries * 5
df$points_convs <- df$conv * 2
df$points_pens <- df$penalties * 3
df$points_drops <- df$drop_kicks * 3



write.csv(df, file = "C:/Users/John/Documents/GitHub/RugbyStats/preprocessed.csv")