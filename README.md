# Blue Cloud Hackathon 2022 - Sea Clearly
This repository contains code created by the team The Particle Trackers for the [Blue Cloud Hackathon 2022](https://hackathon.blue-cloud.org/).

**Team Name**: The Particle Trackers

**Team Leader**: Delphine Lobelle

**Team members**: Claudio Pierard, Cleo Jongedijk, Darshika Manral, Joey Richardson, Laura Gomez-Navarro, Olmo Zavala-Romero, Victor Onink

## Project description
The Particle Trackers is a group of eight early career ocean professionals based in the Netherlands, UK, Switzerland, and the United States. We have co-designed an open science project named Sea Clearly that aims to estimate the origin and destination of inert pollutants that interact with Mediterranean aquaculture cages. Our hackathon case-study focuses on microplastic (0.002 - 5 mm) pollution, however we intend to further develop our model for any inert pollutant data on the BlueCloud server.

Aquaculture farmers and the European Commission aim to provide sustainable, high-quality, high-quantity, safe yields of marine-based food security. We believe that the ‘safety’ aspect is the most important goal, since without safe yields, the other goals cannot be attained. Although there is still ongoing research regarding the potential threats to human health upon consumption of plastic-ingested marine species, proactive and preventative actions are much safer than reactive ones. Sea Clearly will therefore provide a solution for this challenge by identifying the likelihood of aquaculture farms at specific locations to be contaminated by pollutants released from the Mediterranean coast. We also intend to provide pathways of pollutants or gear particles released from aquaculture farms to track their destination and prevent future contamination into surrounding areas (especially marine protected areas) from cages. 

During this hackathon we will implement our solution via forward and back-tracking of particles to and from aquaculture cages, using an open-access Lagrangian particle-tracking framework, OceanParcels (www.oceanparcels.org). We will include 2D surface advection from CMEMS flow data to follow particles transported by ocean currents. We will release modelled particles from the beaches and rivers, based on latest estimates of Mediterranean plastic concentrations (from Lebreton et al. 2019), and run the simulations for one year. For future development, we could implement all BlueCloud pollutant data as the contamination source. When a particle makes contact with an aquaculture cage (from the locations provided on BlueCloud), we will record this as a potential consumption by a species (or trapping by filter-feeders, like shellfish). We will then perform a Bayesian Inference analysis to provide the most likely origin of the particles that reached an aquaculture farm. Finally, we will repeat this entire process with the origin of plastic at an aquaculture farm to indicate the impacts of the farms on the surrounding ecosystems. The output after 6 months’ development on the BlueCloud platform will be to identify the safest locations that can produce the highest-value yields for future Mediterranean aquaculture farms.

Our project contributes to the European Commission’s strategy and innovation action Mission Starfish 2030. Specifically, it supports the implementation of Maritime Spatial Planning and identifies gaps in observations - which we will highlight as requirements to run and validate our model output.

## Repository Contents
This repository contains two Jupyter Notebooks:
- `DataExtraction.ipynb`: This notebook processes and plots data extracted from the Blue Cloud Server
- `Deliverable3_ExampleCase.ipynb`: This contains example simulations and analysis for forward/backward Lagrangian simulations and Bayesian analysis. 
