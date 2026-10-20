def bayes(p_h, p_eh=0.9, p_es=0.1):
    return (p_eh * p_h) / (p_eh * p_h + p_es * (1 - p_h))

print("P(H|ALARM):", round(bayes(0.20), 4), "| P(H|NORMAL):", round(bayes(0.20, 0.1, 0.9), 4))

for p in [0.05, 0.10, 0.20, 0.50, 0.80]:
    print(f"P={p} -> ALARM: {bayes(p):.4f} | NORMAL: {bayes(p, 0.1, 0.9):.4f}")

def hmm_filter(p_h, obs):
    p_s = 1.0 - p_h
    sens = {'ALARM': (0.9, 0.1), 'NORMAL': (0.1, 0.9)}
    
    for t, o in enumerate(obs, 1):
        pred_h = p_h * 0.8 + p_s * 0.1
        pred_s = p_h * 0.2 + p_s * 0.9
        
        un_h, un_s = pred_h * sens[o][0], pred_s * sens[o][1]
        tot = un_h + un_s
        p_h, p_s = un_h / tot, un_s / tot
        
        print(f"T{t} ({o}): Pred P(H)={pred_h:.4f} | Upd P(H)={p_h:.4f}")

hmm_filter(0.20, ['ALARM', 'NORMAL', 'ALARM', 'ALARM'])
