import subprocess
import sys



def kill_background_processes():
    print("\nCleaning up background processes...")
    apps_to_kill = ["SpaceClaim.exe", "fluent.exe", "fluentlauncher.exe", "mpiexec.exe", "hydra_pmi_proxy.exe"]
    for app in apps_to_kill:
        subprocess.call(f"taskkill /F /IM {app} /T", shell=True)


if __name__ == "__main__":
    kill_background_processes()
    sys.exit(1)