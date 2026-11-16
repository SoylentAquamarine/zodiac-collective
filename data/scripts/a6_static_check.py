import re,sys
src=open(sys.argv[1]).read()
def g(p):
    m=re.search(p,src); return m.group(1) if m else None
v4={'seed':g(r'random\.Random\((\d+)\)'),'restarts':g(r'RESTARTS = (\d+)'),'iters':g(r'ITERS_PER_RESTART = (\d+)'),
    'swap_prob':g(r'do_swap = rng\.random\(\) < ([\d.]+)'),
    'history_dependent_restarts':str(bool(re.search(r'perturb_mapping\(best_overall_mapping',src))),
    'single_shared_rng':str(len(re.findall(r'random\.Random\(',src))==1)}
a6={'seed':'20261113+window*1000+restart (per-restart)','restarts':'20','iters':'"unchanged"','swap_prob':'"swap-based" (unspecified)',
    'history_dependent_restarts':'False implied by per-restart seeds','single_shared_rng':'False implied'}
for k in v4: print(f"{k:28s} v4={v4[k]!s:8s} A6={a6[k]}")
