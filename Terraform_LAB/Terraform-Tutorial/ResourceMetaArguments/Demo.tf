provider "google" {
  project     = "dev-ops-project-398806"
  credentials = "${file("credentials.json")}"
  region      = "us-central1"
  zone = "us-central1-c"
}

# locals {
#   compute_names = {developer="us-central1-a", tester="us-central1-b"}
# }
resource "google_compute_instance" "myinstance" {
#   for_each     = tomap(local.compute_names) 
  name         = "my-instance"
  machine_type = "n1-standard-1"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      labels = {
        my_label = "label1"
      }
    }
  }
  // Local SSD disk
  scratch_disk {
    interface = "SCSI"
  }
   network_interface {
    network = "default"
      access_config {

    }
  }
  desired_status = "RUNNING"
  allow_stopping_for_update=true
#    lifecycle {
#     create_before_destroy = true
#   }
}


