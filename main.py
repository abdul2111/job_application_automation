import time
import pandas as pd

# Read job links
def read_job_links(file_path):
    with open(file_path, 'r') as file:
        links = [line.strip() for line in file.readlines() if line.strip()]
    return links

# Placeholder for deciding which resume to use
def select_resume(job_description):
    # Later: Add smart logic here
    return "resumes/Data_Analyst.pdf"

# Placeholder for applying to job
def apply_to_job(link, resume_path):
    print(f"Applying to: {link}")
    print(f"Using resume: {resume_path}")
    # Later: Add Selenium code here
    time.sleep(2)  # simulate wait
    return True

# Save history of applications
def save_application_history(link, resume):
    df = pd.DataFrame([[link, resume, time.strftime('%Y-%m-%d %H:%M:%S')]],
                      columns=["Job Link", "Resume Used", "Applied At"])
    df.to_csv('history.csv', mode='a', header=not pd.io.common.file_exists('history.csv'), index=False)

def main():
    job_links = read_job_links('job_links.txt')
    
    for link in job_links:
        # Later: scrape job description
        job_description = "Sample job description"
        
        resume = select_resume(job_description)
        success = apply_to_job(link, resume)
        
        if success:
            save_application_history(link, resume)

if __name__ == "__main__":
    main()
