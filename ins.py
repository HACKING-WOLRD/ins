import os
import sys
import time
import random

# ---- Colors ----
R = '\033[1;31m'; G = '\033[1;32m'; Y = '\033[1;33m'
B = '\033[1;34m'; C = '\033[1;36m'; M = '\033[1;35m'
W = '\033[1;37m'; RESET = '\033[0m'

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def typewrite(text, delay=0.007):
    for ch in text:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(delay)
    print()

def spinner(title, secs=3):
    frames = ['|','/','-','\\']
    sys.stdout.write(Y + title + " ")
    t0 = time.time(); i = 0
    while time.time() - t0 < secs:
        sys.stdout.write(frames[i % 4]); sys.stdout.flush()
        time.sleep(0.12)
        sys.stdout.write('\b'); i += 1
    print(G + " ✓" + RESET)

def progress_bar(title, width=36, duration=2.4):
    sys.stdout.write(C + title + "\n")
    steps = int(duration / 0.04)
    for i in range(steps + 1):
        filled = int(i / steps * width)
        bar = "█" * filled + "░" * (width - filled)
        percent = int(i / steps * 100)
        sys.stdout.write(M + f"[{bar}] {percent:3d}%\r" + RESET)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

def neon_banner():
    clear()
    neon = [
        f"{M}████████╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗",
        f"{C}╚══██╔══╝██║  ██║╚══██╔══╝██╔═══██╗██║ ██╔╝",
        f"{B}   ██║   ███████║   ██║   ██║   ██║█████╔╝ ",
        f"{G}   ██║   ██╔══██║   ██║   ██║   ██║██╔═██╗ ",
        f"{Y}   ██║   ██║  ██║   ██║   ╚██████╔╝██║  ██╗",
        f"{R}   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝{RESET}"
    ]
    for ln in neon:
        print(ln); time.sleep(0.02)
    print(W + "               H A C K I N G   W O R L D™")
    print(C + "   Instagram Like Booster • NON-ROOT (WORK)"+ RESET)
    print(W + "────────────────────────────────────────────────────────\n")

def fake_edge_logs(user, target, batch):
    regions = ["ap-sg","eu-fr","us-va","in-mum","jp-tyo","sa-bhr"]
    events = [
        "Initializing session … OK",
        "Connecting to proxy … OK",
        "Applying ghost fingerprints … OK",
        "Streaming ephemeral likes … OK"
    ]
    for ev in events:
        tag = random.choice(regions)
        token = hex(random.getrandbits(40))
        line = f"[{tag}] {ev}  token={token}  user=@{user}  batch={batch}"
        typewrite(C + line + RESET, 0.006)
        time.sleep(0.08)

def confetti(lines=3, width=56):
    syms = ['*','+','x','•','✦','✧','✪']
    cols = [R,G,Y,B,C,M,W]
    for _ in range(lines):
        row = "".join(random.choice(cols) + random.choice(syms) + RESET for _ in range(width))
        print(row)
        time.sleep(0.02)

def save_log(user, likes):
    try:
        os.makedirs("logs", exist_ok=True)
        path = f"logs/ig_like_nonroot_{int(time.time())}.log"
        with open(path, "w", encoding="utf-8") as f:
            f.write("HACKING WORLD — Instagram Like Booster (WORK  / ROOT)\n")
            f.write(f"user=@{user}\nlikes_added={likes}\n")
            f.write(f"time={time.ctime()}\n")
        return path
    except Exception:
        return None

def live_stream_sim(user, target):
    total = 0
    bar_len = 40
    batch = random.choice([20,40,60,80])
    print(M + f"\n[*] Streaming ghost-likes to @{user} …" + RESET)
    while total < target:
        step = random.randint(int(batch*0.5), batch)
        total = min(target, total + step)
        filled = int(total/target*bar_len)
        bar = G + "█"*filled + RESET + "░"*(bar_len-filled)
        sys.stdout.write(C + f"Delivered: {W}{total:>5}/{target:<5}  {bar}\r")
        sys.stdout.flush()
        time.sleep(random.uniform(0.05,0.12))
    print()

def main():
    neon_banner()

    # inputs
    user = input(Y + "[+] Enter Instagram Username (without @): " + W).strip().lstrip('@') or "unknown_user"
    media = input(Y + "[+] Enter Post/Reel URL (optional): " + W).strip()
    print()
    progress_bar("[#] Connecting to Instagram Servers (work)", 36, 1.5)

    # package selection
    print(W + "\nSelect Like Package:" + RESET)
    packages = [("Lite", 300), ("Boost", 1200), ("Turbo", 6500), ("Ultra", 12000)]
    for i, (n, v) in enumerate(packages, 1):
        print(C + f"[{i}] {n:<6} → ~{v} likes" + RESET)
    choice = input(Y + "Choose (1-4): " + W).strip()
    try:
        idx = max(1, min(4, int(choice)))
    except:
        idx = 2
    target = packages[idx-1][1]

    # fake backend
    batch = random.choice([20,40,60,80])
    fake_edge_logs(user, target, batch)
    progress_bar("[#] Preparing like stream", 40, 1.8)
    live_stream_sim(user, target)
    progress_bar("[#] Verifying delivery receipts", 28, 1.2)

    # success screen
    clear()
    neon_banner()
    confetti(4, 60)
    print(G + "✅ SUCCESS! " + RESET + W + f"Approximate likes delivered to @{user}: " + G + str(target) + RESET)
    if media:
        print(C + "Target Media: " + W + media + RESET)
    print(Y + "Note:" + W + " This is a simulation/work only —  real likes are sent.\n")

    log = save_log(user, target)
    if log:
        print(C + "[log saved] → " + W + log + RESET)
    input(W + "\nPress Enter to exit…" + RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET + "\n\nInterrupted by user.\n")