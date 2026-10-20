def bayes_formula(p_h, p_e_h, p_e_s):
    p_e = p_e_h * p_h + p_e_s * (1 - p_h)
    return (p_e_h * p_h) / p_e, p_e


p_h_alarm, _ = bayes_formula(0.20, 0.90, 0.10)
p_h_norm, _  = bayes_formula(0.20, 0.10, 0.90)

print(f"P(H|ALARM) = {p_h_alarm:.4f} | P(H|NORMAL) = {p_h_norm:.4f}\n")


print("P(HAZARD) | P(H|ALARM) | P(H|NORMAL)")
for p in [0.05, 0.10, 0.20, 0.50, 0.80]:
    a, _ = bayes_formula(p, 0.90, 0.10)
    n, _ = bayes_formula(p, 0.10, 0.90)
    print(f"{p:<9.2f} | {a:<10.4f} | {n:<10.4f}")


def hmm_filter(p_h, obs, trans, sensor):
    p_s = 1.0 - p_h
    print(f"\n{'T':<3} | {'Obs':<7} | {'Pred P(H)':<10} | {'Upd P(H)':<10} | {'Pred P(S)':<10} | {'Upd P(S)':<10}")
    print("-" * 65)
    
    for t, o in enumerate(obs, 1):
        pred_h = p_h * trans['H'][0] + p_s * trans['S'][0]
        pred_s = p_h * trans['H'][1] + p_s * trans['S'][1]
        
        unnorm_h = pred_h * sensor[o]['H']
        unnorm_s = pred_s * sensor[o]['S']
        tot = unnorm_h + unnorm_s
        
        p_h, p_s = unnorm_h / tot, unnorm_s / tot
        print(f"T{t:<2} | {o:<7} | {pred_h:<10.4f} | {p_h:<10.4f} | {pred_s:<10.4f} | {p_s:<10.4f}")

transitions = {'H': (0.80, 0.20), 'S': (0.10, 0.90)}  
sensor = {'ALARM': {'H': 0.90, 'S': 0.10}, 'NORMAL': {'H': 0.10, 'S': 0.90}}

hmm_filter(0.20, ['ALARM', 'NORMAL', 'ALARM', 'ALARM'], transitions, sensor)