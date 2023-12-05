provider "google" {
  project     = "securitycommandtest"
  credentials = "${file("credentials.json")}"
  region      = "us-central1"
  zone = "us-central1-c"
}
resource "google_storage_bucket" "bucket" {
  name     = "terrabuck978"
  location = "us-central1"
}

resource "google_storage_bucket_object" "archive" {
  name   = "MyTerraformFunction"
  bucket = google_storage_bucket.bucket.name
  source = "function-source.zip"
}

resource "google_cloudfunctions_function" "function-by-terraform" {
  name        = "function-by-terraform"
  description = "This is first Terraform function"
  runtime     = "java11"

  available_memory_mb   = 256
  source_archive_bucket = google_storage_bucket.bucket.name
  source_archive_object = google_storage_bucket_object.archive.name
  trigger_http          = true
  entry_point           = "com.example.Example"
}

# IAM entry for all users to invoke the function
resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = google_cloudfunctions_function.function-by-terraform.project
  region         = google_cloudfunctions_function.function-by-terraform.region
  cloud_function = google_cloudfunctions_function.function-by-terraform.name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}