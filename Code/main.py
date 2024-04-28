from Simulations import *
import sys

print("start")

output = """Select the simulation you want to run (separated by space):
            1. Varying N for Barnes-Hut
            2. Varying theta for Barnes-Hut
            3. Varying n_leaf for Barnes-Hut
            4. Comparing Fast Multipole Method and Barnes-Hut
            5. Varying N for Fast Multipole Method
            6. Varying p for Fast Multipole Method
            7. Varying levels for Fast Multipole Method
            8. Varying n_leaf for Fast Multipole Method
            9. Comparing Fixed and Adaptive Fast Multipole Method
            10. Exit
            """
try:
    simul_list = [int(i) for i in input(output).split(" ")]
except:
    print("End programme")
    sys.exit(0)


print(f"Running {simul_list}")
for simul in simul_list:
    if simul==1:
        try:
            bh_varying_n()
        except Exception as error:
            print(print("An exception occurred:", error) )
    if simul==2:
        try:
            bh_varying_theta()
        except Exception as error:
            print(print("An exception occurred:", error) )
    if simul==3:
        try:
            bh_varying_leaf()
        except Exception as error:
            print(print("An exception occurred:", error) )
    if simul==4:
        try:
            fmm_vs_bh()
        except Exception as error:
            print(print("An exception occurred:", error) )
    if simul==5:
        fmm_varying_n()
        try:
            fmm_varying_n()
        except Exception as error:
            print(print("An exception occurred:", error) )
    if simul==6:
        try:
            fmm_varying_p()
        except Exception as error:
            print(print("An exception occurred:", error) )
    if simul==7:
        try:
            fmm_varying_levels()
        except Exception as error:
            print(print("An exception occurred:", error) )
    if simul==8:
        try:
            fmm_varying_leaf()
        except Exception as error:
            print(print("An exception occurred:", error) )
    if simul==9:
        try:
            fmm_fixed_vs_adaptive()
        except Exception as error:
            print(print("An exception occurred:", error) )
    if simul==10:
        print("End programme")
        sys.exit(0)
