import tkinter as tk
from tkinter import messagebox
import random

# ==========================================
#   DEFAULT SETTINGS
# ==========================================
DEFAULT_CONFIG = {
    "system_pass": "rakesh68",
    
    # Folder 1 Settings
    "folder_name": "projectSync_SiLiConBuild_Stable.zip",
    "folder_pass": "14327",
    "clue_text": "Blood runs red into the blue of sky \nThe sun burns gold, then rests as green grass.\nNight drains black until dawn turns it pale blue.\nFire fades orange, leaving earth in brown.",
    
    # Folder 2 Settings (NEW)
    "folder2_name": " DCS_Malfunction_2019_report.pdf",
    "folder2_pass": "",
    "folder2_clue": "VIDEO FEED DECRYPTED:\n\nGuard shift changes at 03:00.\nKeypad code: 1-9-8-4",

    # Clue File Settings (NEW)
    "file_name": "readme_urgent.txt",
    "file_text": "TO WHOEVER FINDS THIS:\n\nDo not trust the system logs.\nThe red wire is the decoy.\n\n- Dr. V"
}

def generate_log_line():
    hex_data = ' '.join([random.choice(['0xAF', '3E', 'C1', 'FE', '00', 'BD']) for _ in range(5)])
    actions = ["DECRYPTING...", "BYPASSING HASH...", "MEMORY DUMP...", "KEY EXCHANGE...", "BRUTE FORCE..."]
    return f"> [{hex_data}] : {random.choice(actions)}"

class EscapeOS:
    def __init__(self, root):
        self.root = root
        self.root.title("TERMINAL_VOID_OS")
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True) 
        self.root.configure(bg="black")
        
        self.config = DEFAULT_CONFIG.copy()

        # --- KEY BINDINGS ---
        self.root.bind("<Control-Alt-space>", lambda e: self.root.destroy()) 
        self.root.bind("<Win_L>", lambda e: "break") 
        self.root.bind("<Alt-Tab>", lambda e: "break")
        self.root.bind("<Control-Escape>", lambda e: "break")

        self.root.bind("<F12>", lambda e: self.open_admin_panel())
        self.root.bind("<F11>", lambda e: self.quick_lock())

        self.boot_sequence()

    # ==========================================
    #   QUICK LOCK (F11)
    # ==========================================
    def quick_lock(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.configure(bg="black")
        self.show_login()

    # ==========================================
    #   SECTION 1: ADMIN PANEL (F12)
    # ==========================================
    def open_admin_panel(self):
        self.root.attributes("-topmost", False)
        admin_win = tk.Toplevel(self.root)
        admin_win.title("GAME MASTER CONTROL")
        admin_win.geometry("600x750") # Made taller for new options
        admin_win.configure(bg="#222")
        admin_win.bind("<Destroy>", lambda e: self.root.attributes("-topmost", True))
        
        # Scrollable Canvas for Admin Panel
        canvas = tk.Canvas(admin_win, bg="#222", highlightthickness=0)
        scrollbar = tk.Scrollbar(admin_win, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#222")

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        tk.Label(scroll_frame, text="[ GAME MASTER CONFIG ]", fg="white", bg="#222", font=("Arial", 16, "bold")).pack(pady=10)

        def create_input(label, key):
            tk.Label(scroll_frame, text=label, fg="#aaa", bg="#222").pack(anchor="w", padx=20)
            entry = tk.Entry(scroll_frame, font=("Arial", 10), width=50)
            entry.insert(0, self.config[key])
            entry.pack(pady=2, padx=20)
            return entry
        
        def create_text_input(label, key):
            tk.Label(scroll_frame, text=label, fg="#aaa", bg="#222").pack(anchor="w", padx=20)
            txt = tk.Text(scroll_frame, height=3, width=50, font=("Arial", 10))
            txt.insert("1.0", self.config[key])
            txt.pack(pady=2, padx=20)
            return txt

        # --- SYSTEM ---
        tk.Label(scroll_frame, text="--- SYSTEM ---", fg="gold", bg="#222").pack(pady=(10,0))
        e_sys_pass = create_input("System Login Password:", "system_pass")

        # --- FOLDER 1 ---
        tk.Label(scroll_frame, text="--- FOLDER 1 (Top) ---", fg="gold", bg="#222").pack(pady=(10,0))
        e_fold_name = create_input("Name:", "folder_name")
        e_fold_pass = create_input("Password:", "folder_pass")
        e_clue = create_text_input("Clue Content:", "clue_text")

        # --- FOLDER 2 ---
        tk.Label(scroll_frame, text="--- FOLDER 2 (Middle) ---", fg="gold", bg="#222").pack(pady=(10,0))
        e_fold2_name = create_input("Name:", "folder2_name")
        e_fold2_pass = create_input("Password:", "folder2_pass")
        e_fold2_clue = create_text_input("Clue Content:", "folder2_clue")

        # --- CLUE FILE ---
        tk.Label(scroll_frame, text="--- CLUE FILE (Bottom) ---", fg="gold", bg="#222").pack(pady=(10,0))
        e_file_name = create_input("File Name:", "file_name")
        e_file_text = create_text_input("File Content:", "file_text")

        def save_and_reset():
            self.config["system_pass"] = e_sys_pass.get()
            
            self.config["folder_name"] = e_fold_name.get()
            self.config["folder_pass"] = e_fold_pass.get()
            self.config["clue_text"] = e_clue.get("1.0", "end-1c")
            
            self.config["folder2_name"] = e_fold2_name.get()
            self.config["folder2_pass"] = e_fold2_pass.get()
            self.config["folder2_clue"] = e_fold2_clue.get("1.0", "end-1c")

            self.config["file_name"] = e_file_name.get()
            self.config["file_text"] = e_file_text.get("1.0", "end-1c")
            
            admin_win.destroy()
            self.quick_lock()
            messagebox.showinfo("ADMIN", "Settings Updated! System Locked.")

        tk.Button(scroll_frame, text="SAVE & LOCK SYSTEM", command=save_and_reset, bg="green", fg="white", font=("Arial", 12, "bold")).pack(pady=20)
        tk.Label(scroll_frame, text="Shortcuts: F11=Reset | Ctrl+Alt+Space=Quit", fg="#777", bg="#222").pack(pady=10)

    # ==========================================
    #   SECTION 2: BOOT SEQUENCE
    # ==========================================
    def boot_sequence(self):
        self.boot_lbl = tk.Label(self.root, text="", fg="#00ff00", bg="black", font=("Courier New", 14), justify="left")
        self.boot_lbl.pack(expand=True, fill="both", padx=50, pady=50)
        
        boot_lines = [
            "BIOS CHECK... OK",
            "INITIALIZING SECURE KERNEL...",
            "LOADING DRIVERS...",
            "...................",
            "ERROR: UNEXPECTED SHUTDOWN DETECTED",
            "WARNING: FILE SYSTEM INTEGRITY COMPROMISED",
            "BOOTING INTO EMERGENCY MODE..."
        ]
        self.animate_boot(boot_lines, 0)

    def animate_boot(self, lines, index):
        if index < len(lines):
            line = lines[index]
            current = self.boot_lbl.cget("text")
            if "ERROR" in line or "WARNING" in line:
                self.boot_lbl.config(fg="red")
            self.boot_lbl.config(text=current + "\n" + line)
            self.root.after(random.randint(200, 600), lambda: self.animate_boot(lines, index + 1))
        else:
            self.root.after(1000, self.show_login)

    # ==========================================
    #   SECTION 3: LOGIN SCREEN
    # ==========================================
    def show_login(self):
        try: self.boot_lbl.destroy()
        except: pass
        
        self.login_frame = tk.Frame(self.root, bg="black")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        tk.Label(self.login_frame, text="SYSTEM LOCKED", fg="red", bg="black", font=("Courier New", 30, "bold")).pack(pady=20)
        tk.Label(self.login_frame, text="ENTER PASSWORD:", fg="white", bg="black", font=("Courier New", 12)).pack()
        
        self.pass_entry = tk.Entry(self.login_frame, show="*", font=("Arial", 24), bg="#111", fg="red", insertbackground="red", justify="center")
        self.pass_entry.pack(pady=10)
        self.pass_entry.focus_set()
        self.pass_entry.bind("<Return>", self.check_login)
        self.pass_entry.bind("<Key>", self.update_login_logs)
        
        tk.Button(self.login_frame, text="LOGIN", command=self.check_login_btn, bg="#440000", fg="white").pack(pady=10)
        
        self.login_log_lbl = tk.Label(self.login_frame, text="WAITING FOR INPUT...", fg="#33ff33", bg="black", font=("Courier New", 10), height=5, anchor="sw", justify="left")
        self.login_log_lbl.pack(fill="x", pady=20)

        tk.Label(self.root, text="[ ]  [ ]", fg="#333", bg="black").pack(side="bottom", pady=20)

    def update_login_logs(self, event):
        current_text = self.login_log_lbl.cget("text")
        lines = current_text.split("\n")
        if len(lines) > 4: lines.pop(0) 
        lines.append(generate_log_line())
        self.login_log_lbl.config(text="\n".join(lines))

    def check_login(self, event):
        self.check_login_btn()

    def check_login_btn(self):
        if self.pass_entry.get() == self.config["system_pass"]:
            for widget in self.root.winfo_children():
                widget.destroy()
            self.play_access_animation()
        else:
            self.pass_entry.delete(0, tk.END)
            messagebox.showwarning("ACCESS DENIED", "INCORRECT PASSWORD")

    def play_access_animation(self):
        self.anim_lbl = tk.Label(self.root, text="", fg="#00ff00", bg="black", font=("Courier New", 14, "bold"), justify="left", anchor="w")
        self.anim_lbl.place(x=50, rely=0.5, anchor="w") 
        
        sequence = [
            "ACCESS GRANTED.", "VERIFYING ADMIN PRIVILEGES... OK", "DECRYPTING ROOT DIRECTORY... 100%", 
            "LOADING USER PROFILE... DONE", ".................................", 
            "WARNING: UNKNOWN PROCESS DETECTED", "ALERT: FILE INTEGRITY 45%", 
            "ERROR: MEMORY OVERFLOW IN SECTOR 7", ".................................", 
            "CRITICAL FAILURE DETECTED", "SYSTEM COMPROMISED", 
            "INITIATING EMERGENCY PROTOCOL...", "SYSTEM HALT."
        ]
        self.run_animation_step(sequence, 0)

    def run_animation_step(self, lines, index):
        if index < len(lines):
            if index < 5: self.anim_lbl.config(fg="#00ff00")
            elif index < 9: self.anim_lbl.config(fg="#ffaa00")
            else: self.anim_lbl.config(fg="#ff0000")
            
            current_text = self.anim_lbl.cget("text")
            if current_text.count("\n") > 15: current_text = current_text.split("\n", 1)[1]
            self.anim_lbl.config(text=current_text + "\n" + lines[index])
            self.root.after(200, lambda: self.run_animation_step(lines, index + 1))
        else:
            self.root.after(1000, self.anim_lbl.destroy)
            self.root.after(1000, self.launch_desktop)

    # ==========================================
    #   SECTION 4: VIRTUAL DESKTOP
    # ==========================================
    def launch_desktop(self):
        self.canvas = tk.Canvas(self.root, bg="#050505", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.draw_grid()
        self.start_digital_noise()
        
        taskbar = tk.Frame(self.root, bg="#cc0000", height=50)
        taskbar.place(relx=0, rely=1.0, anchor="sw", relwidth=1.0, height=50)
        tk.Label(taskbar, text="SYSTEM AT CRITICAL STATE", fg="white", bg="#cc0000", font=("Courier New", 14, "bold"), padx=20).pack(side="left", fill="y")
        
        monitor = tk.Frame(self.root, bg="black", bd=1, relief="sunken")
        monitor.place(relx=0.98, rely=0.02, anchor="ne", width=200, height=100)
        tk.Label(monitor, text="CPU LOAD: 99%", fg="red", bg="black", font=("Courier New", 10)).pack(pady=10)
        tk.Label(monitor, text="MEM LEAK: DETECTED", fg="red", bg="black", font=("Courier New", 10)).pack()

        # --- ICONS ---
        start_x, start_y = 40, 40
        spacing = 140 

        # 1. First Puzzle Folder
        self.create_icon(start_x, start_y, "📁", self.config["folder_name"], lambda: self.open_folder_puzzle(1), True)
        
        # 2. Second Puzzle Folder (NEW)
        self.create_icon(start_x, start_y + spacing, "📁", self.config["folder2_name"], lambda: self.open_folder_puzzle(2), True)
        
        # 3. Standalone Clue File (NEW)
        self.create_icon(start_x, start_y + spacing*2, "📄", self.config["file_name"], self.open_file_clue, False)
        
        # 4. Decoy
        self.create_icon(start_x, start_y + spacing*3, "⚙️", "config.sys", lambda: messagebox.showerror("Error", "Access Denied"))
        
        # 5. Recycle Bin (Nudged)
        self.create_icon(start_x, start_y + spacing*4, "🗑️", "Recycle Bin", lambda: messagebox.showinfo("Info", "Empty"), text_nudge=-90)

    # --- HELPERS ---
    def draw_grid(self):
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        for i in range(0, w, 50): self.canvas.create_line(i, 0, i, h, fill="#110000")
        for i in range(0, h, 50): self.canvas.create_line(0, i, w, i, fill="#110000")

    def start_digital_noise(self):
        try:
            x, y = random.randint(0, self.root.winfo_screenwidth()), random.randint(0, self.root.winfo_screenheight())
            txt = self.canvas.create_text(x, y, text=random.choice(["0", "1", "ERR"]), fill="#330000", font=("Courier New", 12, "bold"))
            self.root.after(3000, lambda: self.canvas.delete(txt))
            self.root.after(50, self.start_digital_noise)
        except: pass

    def create_icon(self, x, y, icon, label, cmd, is_target=False, text_nudge=0):
        f = tk.Frame(self.root, bg="#050505", cursor="hand2")
        f.place(x=x, y=y)
        icon_color = "#ff0000" if is_target else "#990000"
        text_color = "white" if is_target else "#ffcccc" 
        
        l_icon = tk.Label(f, text=icon, fg=icon_color, bg="#050505", font=("Arial", 50))
        l_icon.pack(side="top", anchor="center")
        
        pad_left = abs(text_nudge) if text_nudge > 0 else 0
        pad_right = abs(text_nudge) if text_nudge < 0 else 0
        
        l_text = tk.Label(f, text=label, fg=text_color, bg="#050505", font=("Courier New", 10, "bold"), justify="center")
        l_text.pack(side="top", anchor="center", pady=(5,0), padx=(pad_left, pad_right))
        
        def on_enter(e):
            f.config(bg="#220000")
            l_icon.config(bg="#220000", fg="#ff3333")
            l_text.config(bg="#220000", fg="white")
        def on_leave(e):
            f.config(bg="#050505")
            l_icon.config(bg="#050505", fg=icon_color)
            l_text.config(bg="#050505", fg=text_color)
        for w in [f, l_icon, l_text]:
            w.bind("<Button-1>", lambda e: cmd())
            w.bind("<Enter>", on_enter)
            w.bind("<Leave>", on_leave)

    # ==========================================
    #   SECTION 5: GENERIC FOLDER PUZZLE LOGIC
    # ==========================================
    def open_folder_puzzle(self, folder_id):
        # Determine which folder settings to use
        if folder_id == 1:
            target_pass = self.config["folder_pass"]
            target_clue = self.config["clue_text"]
            title = "SECURE FOLDER 1"
        else:
            target_pass = self.config["folder2_pass"]
            target_clue = self.config["folder2_clue"]
            title = "SECURE FOLDER 2"

        self.root.attributes("-topmost", False)
        self.popup = tk.Toplevel(self.root)
        self.popup.geometry("450x350+500+300")
        self.popup.configure(bg="#111", highlightthickness=2, highlightbackground="red")
        self.popup.overrideredirect(True)
        self.popup.bind("<Destroy>", lambda e: self.root.attributes("-topmost", True))
        
        tk.Label(self.popup, text=title, fg="red", bg="#111", font=("Courier New", 16, "bold")).pack(pady=15)
        
        entry = tk.Entry(self.popup, show="*", font=("Arial", 20), justify="center", bg="black", fg="red")
        entry.pack(pady=5)
        entry.focus_set()

        log_lbl = tk.Label(self.popup, text="AWAITING KEY...", fg="red", bg="#111", font=("Courier New", 9), height=5, anchor="sw", justify="left")
        log_lbl.pack(fill="x", padx=20, pady=10)
        
        # Local log update function
        def update_logs(event):
            txt = log_lbl.cget("text").split("\n")
            if len(txt) > 4: txt.pop(0)
            txt.append(f"> HEX_DUMP [{random.randint(10,99)}]...")
            log_lbl.config(text="\n".join(txt))
        entry.bind("<Key>", update_logs)

        def check_code():
            if entry.get() == target_pass:
                self.popup.destroy()
                self.show_popup_clue(target_clue)
            else:
                entry.delete(0, tk.END)
                messagebox.showerror("ERROR", "INVALID PASSCODE")

        entry.bind("<Return>", lambda e: check_code())
        tk.Button(self.popup, text="UNLOCK", command=check_code, bg="#330000", fg="white").pack(pady=5)
        tk.Button(self.popup, text="CANCEL", command=self.popup.destroy, bg="#111", fg="#555", bd=0).pack()

    # ==========================================
    #   SECTION 6: STANDALONE CLUE FILE
    # ==========================================
    def open_file_clue(self):
        self.show_popup_clue(self.config["file_text"])

    def show_popup_clue(self, text_content):
        self.root.attributes("-topmost", False)
        win = tk.Toplevel(self.root)
        win.geometry("600x400+400+300")
        win.configure(bg="black", highlightthickness=2, highlightbackground="#00ff00")
        win.overrideredirect(True)
        win.bind("<Destroy>", lambda e: self.root.attributes("-topmost", True))
        
        tk.Label(win, text="--- DECRYPTED DATA ---", fg="#00ff00", bg="black", font=("Courier New", 12)).pack(pady=20)
        tk.Label(win, text=text_content, fg="white", bg="black", font=("Courier New", 14), justify="center").pack(expand=True)
        tk.Button(win, text="CLOSE", command=win.destroy, bg="#222", fg="white").pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = EscapeOS(root)
    root.mainloop()