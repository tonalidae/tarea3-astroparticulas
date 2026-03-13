"""
Descarga los archivos de salida del modelo CORHEL-CME del CCMC.

Uso:
    python download_ccmc.py --email tu@correo.com --password tuPassword

Run: StephanieCarolina_CelyRodriguez_030726_SH_1
"""

import argparse
import getpass
import sys
import time
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("Instala requests: pip install requests")

# ── Configuración ────────────────────────────────────────────────────────────
RUN_NUMBER   = "StephanieCarolina_CelyRodriguez_030726_SH_1"
CCMC_BASE    = "https://ccmc.gsfc.nasa.gov"
LOGIN_URL    = f"{CCMC_BASE}/ror/results/login.php"
DOWNLOAD_URL = f"{CCMC_BASE}/ror/api/get_run_file.php"
OUTPUT_DIR   = Path("data/ccmc/corhel")

FILES = [
    # ── hel_bc/ – condiciones de frontera del heliosfera ────────────────────
    "hel_bc/bp_r0.hdf",
    "hel_bc/bp_r0000001.hdf",
    "hel_bc/br_r0.hdf",
    "hel_bc/br_r0000001.hdf",
    "hel_bc/bt_r0.hdf",
    "hel_bc/bt_r0000001.hdf",
    "hel_bc/rho_r0.hdf",
    "hel_bc/rho_r0000001.hdf",
    "hel_bc/t_r0.hdf",
    "hel_bc/t_r0000001.hdf",
    "hel_bc/vp_r0.hdf",
    "hel_bc/vp_r0000001.hdf",
    "hel_bc/vr_r0.hdf",
    "hel_bc/vr_r0000001.hdf",
    "hel_bc/vt_r0.hdf",
    "hel_bc/vt_r0000001.hdf",
    "hel_bc/zero.hdf",
    # ── corona_a/quantities_at_r1/solar_wind_mhd/ – viento solar en r1 ─────
    "corona_a/quantities_at_r1/solar_wind_mhd/bp_r1.hdf",
    "corona_a/quantities_at_r1/solar_wind_mhd/br_r1.hdf",
    "corona_a/quantities_at_r1/solar_wind_mhd/bt_r1.hdf",
    "corona_a/quantities_at_r1/solar_wind_mhd/rho_r1.hdf",
    "corona_a/quantities_at_r1/solar_wind_mhd/t_r1.hdf",
    "corona_a/quantities_at_r1/solar_wind_mhd/vp_r1.hdf",
    "corona_a/quantities_at_r1/solar_wind_mhd/vr_r1.hdf",
    "corona_a/quantities_at_r1/solar_wind_mhd/vt_r1.hdf",
]


def login(session: requests.Session, email: str, password: str) -> bool:
    """Inicia sesión en el CCMC y devuelve True si fue exitoso."""
    # Obtener token CSRF si la página lo requiere
    resp = session.get(LOGIN_URL, timeout=30)
    resp.raise_for_status()

    payload = {"email": email, "password": password, "submit": "Login"}
    resp = session.post(LOGIN_URL, data=payload, timeout=30, allow_redirects=True)

    # Verificar éxito: la página no debería contener el formulario de login
    if "password" in resp.text.lower() and "invalid" in resp.text.lower():
        return False
    if resp.url and "login" in resp.url and resp.status_code == 200:
        # Podría seguir en la página de login si falló
        if "incorrect" in resp.text.lower() or "invalid" in resp.text.lower():
            return False
    return True


def download_file(session: requests.Session, relative_path: str, retries: int = 3) -> bool:
    dest = OUTPUT_DIR / relative_path
    dest.parent.mkdir(parents=True, exist_ok=True)

    if dest.exists() and dest.stat().st_size > 100:
        print(f"  [skip] {relative_path}  (ya existe)")
        return True

    url = f"{DOWNLOAD_URL}?runnumber={RUN_NUMBER}&filename={relative_path}"

    for attempt in range(1, retries + 1):
        try:
            resp = session.get(url, timeout=60, stream=True)
            resp.raise_for_status()

            content = resp.content

            # Detectar respuesta HTML (error o redirect a login)
            if b"<html" in content[:200].lower():
                if b"login" in content[:500].lower():
                    print(f"  [auth] {relative_path}: sesión expirada, reintenta con login")
                else:
                    print(f"  [error] {relative_path}: respuesta HTML inesperada")
                return False

            dest.write_bytes(content)
            print(f"  [ok]   {relative_path}  ({len(content)/1024:.0f} kB)")
            return True

        except requests.HTTPError as exc:
            print(f"  [HTTP {exc.response.status_code}] {relative_path}  intento {attempt}/{retries}")
        except requests.ConnectionError as exc:
            print(f"  [conexión] {relative_path}: {exc}  intento {attempt}/{retries}")
        except requests.Timeout:
            print(f"  [timeout] {relative_path}  intento {attempt}/{retries}")

        if attempt < retries:
            time.sleep(3 * attempt)

    return False


def main():
    parser = argparse.ArgumentParser(description="Descarga archivos CORHEL-CME del CCMC.")
    parser.add_argument("--email",    help="Correo registrado en CCMC")
    parser.add_argument("--password", help="Contraseña CCMC (se pedirá si no se pasa)")
    args = parser.parse_args()

    email    = args.email    or input("Email CCMC: ").strip()
    password = args.password or getpass.getpass("Password CCMC: ")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})

    print("\nIniciando sesión en CCMC...")
    try:
        ok = login(session, email, password)
    except Exception as exc:
        sys.exit(f"Error al conectar con CCMC: {exc}")

    if not ok:
        sys.exit("Login fallido. Verifica tu email y contraseña en https://ccmc.gsfc.nasa.gov")

    print(f"Sesión iniciada. Descargando {len(FILES)} archivos a {OUTPUT_DIR.resolve()}\n")

    succeeded, failed = [], []
    for i, path in enumerate(FILES, 1):
        print(f"[{i:02d}/{len(FILES)}] {path}")
        if download_file(session, path):
            succeeded.append(path)
        else:
            failed.append(path)

    print(f"\n── Resumen {'─'*40}")
    print(f"  Descargados : {len(succeeded)}/{len(FILES)}")
    if failed:
        print(f"  Fallidos ({len(failed)}):")
        for f in failed:
            print(f"    {f}")
        print(
            "\nPara los fallidos, usa 'Request output data in bulk' en:\n"
            f"  https://ccmc.gsfc.nasa.gov/ror/results/viewrun.php?runnumber={RUN_NUMBER}"
        )
        sys.exit(1)
    else:
        print("  Todos los archivos descargados correctamente.")
        print(f"\nArchivos guardados en: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
