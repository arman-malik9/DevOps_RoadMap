provider "google" {
  project     = "dev-ops-project-398806"
  credentials = "${file("credentials.json")}"
  region      = "us-central1"
  zone = "us-central1-c"
}

resource "google_compute_instance" "myinstance" {
  name         = "terraform-test"
  machine_type = "n1-standard-1"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      labels = {
        my_label = "value"
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

 provisioner "remote-exec" {
    connection {
      host        = google_compute_instance.myinstance.network_interface[0].access_config[0].nat_ip
      type        = "ssh"
      user        = "devopseng0789@gmail.com"
      timeout     = "500s"
      private_key = file("./mykey")
      host_key = file("./mykey.pub")
    }
    inline = [
      "sudo su",
      "sudo apt -y install nginx",
      "mkdir arman"

    ]
  }

  # service_account {
  #   email  = "157786403963-compute@developer.gserviceaccount.com"
  #   scopes = ["compute-ro"]
  # }
  # metadata = {
  #   ssh-keys = "${"devopseng0789@gmail.com"}:${file("./mykey.pub")}"
  #}

}