library(tidyverse)
#csv = read.csv("/home/mateusz/ekspolracja_danych/data_file.csv")
gapminder <- read_csv("/home/mateusz/ekspolracja_danych/data_file.csv",
                      col_types = cols(
                        Price = col_integer(),
                        Auction	= col_character(),
                        Lot_number = col_integer(),
                        Date_of_sale = col_character(),	
                        Year = col_integer(),	
                        VIN	= col_character(),
                        Condition	= col_character(),
                        Engine = col_character(),
                        Mileage = col_character(),	
                        Seller = col_character(),	
                        Documents	= col_character(),
                        Location = col_character(),
                        Primary_Damage = col_character(),
                        Secondary_Damage = col_character(),	
                        Estimated_Retail_Value = col_integer(),
                        Estimated_Repair_Cost = col_character(),
                        Transmission = col_character(),
                        Body_color = col_character(),
                        Drive = col_character(),
                        Fuel = col_character(),
                        Keys = col_character(),
                        Notes = col_character()
                      ))
print(gapminder["Transmission"])
#install.packages("ggplot2")
library(ggplot2)
#print(type(gapminder["Transmission"]))

# p<-ggplot(data=gapminder["Transmission"], aes(x=dose, y=len)) +
#   geom_bar(stat="identity")
# p
# gapminder["Drive"] = gsub("-", " ", gapminder["Drive"])
gapminder$Drive <- gsub("-", " ", gapminder$Drive)
gapminder %>% group_by(Transmission) %>% summarise( number = n() ) -> transmission
gapminder %>% group_by(Drive) %>% summarise( number = n() ) -> drive
gapminder %>% group_by(Primary_Damage) %>% summarise( number = n() ) -> primary_damage
print(primary_damage)

ggplot(primary_damage, aes(x=Primary_Damage, y=number)) + 
  geom_bar(stat = "identity", width=0.4)
# print(drive)
# print(transmission)
ggplot(drive, aes(x=Drive, y=number)) +
  geom_bar(stat = "identity", fill="green")

ggplot(transmission, aes(x=number, y=Transmission)) +
  geom_bar(stat = "identity", fill="blue", show.legend = TRUE, orientation = "y")


# x <- sample(c("Win","Linux","Mac"), 100, replace=TRUE)
# barplot(table(x))

# p<-ggplot(data=drive) +
#   geom_bar(stat="identity")
# p

# install.packages("devtools")
# install_github("easyGgplot2", "kassambara")

# library(devtools)
# # library(easyGgplot2)
# ggplot2.barplot(data=primary_damage, xName=c[0], yName=c[1])
# 