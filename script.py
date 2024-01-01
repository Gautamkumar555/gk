def hii():
        import os
        from datetime import datetime, timedelta
        
        # ------------------ SETTINGS ------------------
        username = "gautamkumar555"
        email = "gk772269@gmail.com"
        repo_link = "https://github.com/Gautamkumar555/gk"  # <-- use your actual repo link
        commit_freq = 2  # commits per day
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 12, 31)
        # ----------------------------------------------
        
        # Set up git config
        os.system(f"git config user.name \"{username}\"")
        os.system(f"git config user.email \"{email}\"")
        
        # Initialize git repo if not already done
        os.system("git init")
        
        # Create a simple file and prepare for writing logs
        commit_file = "commit.txt"
        open(commit_file, "w").close()
        
        # Iterate from start_date to end_date
        current_day = start_date
        commit_count = 1
        
        while current_day <= end_date:
            for i in range(commit_freq):
                with open(commit_file, "a") as f:
                    f.write(f"Commit #{commit_count} on {current_day.strftime('%Y-%m-%d')}\n")
        
                os.system("git add .")
        
                # Set time (e.g., 12:15:10 PM)
                commit_time = current_day.strftime("%Y-%m-%d 12:15:10")
                commit_msg = f"commit #{commit_count}"
                os.system(f'git commit --date="{commit_time}" -m "{commit_msg}"')
        
                print(f"{commit_msg}: {commit_time}")
                commit_count += 1
        
            current_day += timedelta(days=1)
        
        # Set or reset remote
        os.system("git remote remove origin > /dev/null 2>&1 || true")
        os.system(f"git remote add origin {repo_link}")
        os.system("git branch -M main")
        
        # Push to GitHub
        os.system("git push -u origin main -f")
  
  
hii()
hii()
hii()
hii()
