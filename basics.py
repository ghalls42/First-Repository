# ##basic variable assignment

# myVar = 4.0 * (5-3)
# myVarBool = True
# myVarBool2 = (myVar == 10)


# ##if else statement
# if myVar <3:
#     print('Less than 3')
# else: 
#     print('Greater than 3')
    
# ##example of a string
# mystring = 'this is a string'
#     ##udemy course has a ton of cool things you can do to mainpulate strings
    
# ##udemy course section 5
#     #if statements
#     #for loops
#     #while loops



##testing out coolprop
import CoolProp.CoolProp as CP
fluid = 'Water'
pressure_at_critical_point = CP.PropsSI(fluid,'pcrit')
# Massic volume (in m^3/kg) is the inverse of density
# (or volumic mass in kg/m^3). Let's compute the massic volume of liquid
# at 1bar (1e5 Pa) of pressure
vL = 1/CP.PropsSI('D','P',1e5,'Q',0,fluid)
# Same for saturated vapor
vG = 1/CP.PropsSI('D','P',1e5,'Q',1,fluid)