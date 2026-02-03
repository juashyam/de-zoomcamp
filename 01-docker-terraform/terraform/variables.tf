variable "project_id" {
  description = "The GCP project ID"
  default     = "terraform-486015"
}

variable "region" {
  description = "The GCP region"
  default     = "us-central1"
}

variable "zone" {
  description = "The GCP zone"
  default     = "us-central1-c"
}

variable "location" {
  description = "The GCP location for storage bucket"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "The BigQuery dataset name"
  default     = "demo_dataset"
}

variable "bucket_name" {
  description = "The GCS bucket name"
  default     = "terraform-486015-terra-bucket"
}