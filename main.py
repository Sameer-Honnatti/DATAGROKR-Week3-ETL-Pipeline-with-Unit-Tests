from etl.pipeline import run_pipeline

def main():
    print("=" * 55)
    print("       DATA GROKR WEEK 3 - ETL PIPELINE")
    print("=" * 55)

    try:
        output_file = run_pipeline()
        print(f"\nETL pipeline completed successfully.")
        print(f"Output file: {output_file}")
    except Exception as error:
        print(f"\nETL pipeline failed: {error}")

if __name__ == "__main__":
    main()