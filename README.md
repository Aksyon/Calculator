# Calculator
There are two calculators in this module: CaloriesCalculator and
CashCalculator.

CaloriesCalculator record calories consumption, control the amount
of day income calories by calculating the rest of calories for
achieving the day limit.

CashCalculator record cash spending, summarize them and calculate
rest of money that you can spend during day.

Day and week statistics are available in both of calculators.

Inheritance is the main OOP technolodgy that used in these modules.

Author: https://github.com/Aksyon 

How to start program:
1) Import module CalculatorLogic
2) Create object by using <object name> = <calculator_name>(limit), 
where calculator_name is CashCalculator or CaloriesCalculator
3) Add some records by using:
    <objecct name>.add_record(Records(amount = .., comment = '..', date = '..')),
    if the record about today, it is allowed to skip the date.
4) Available methods are:
get_today_cash_remained('currency'),
get_calories_remained,
get_week_stats.

Copyright (C) <2022>  <Aleksandr Aksyonov>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.