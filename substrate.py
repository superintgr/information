from torch.utils.data import Dataset
import torch

class Information(Dataset):
    def __init__(self, input, output):
        self.source = torch.stack(input)
        self.transducer = torch.stack(output)
      
    def __getitem__(self, variable):
        return self.source[variable], self.transducer[variable]
      
    def __len__(self):
        return len(self.source)


"""Features and logics:
phonon <- condensed @ matter : collective excitement of periodic arrangement, elastic medium containing molecules or atomic components, 
quantum mechanical quantization : modes of vibrations, elastic structure of interacting particles := excited state

- it can be thought of as quantized sound waves, whereas photons are quantized light waves.
- however phonons are emmergent phenomena whereas photons can be individually detected!

photon yields:
- number of events / number of detected
- emmitted / absorbed

efficiency:
- incident photon to converted electron (IPCE) ratio of a photosensitive device
- it may refer to the TMR effect of a magnetic tunnel junction.

see : [thermoelectric, generator, cooling]
[Photon] / counting is a technique in which individual photons are counted using a single-photon detector (SPD). A single-photon detector emits a pulse of signal for each detected photon. The counting efficiency is determined by the quantum efficiency and the system's electronic losses.
/ Photon [counting] eliminates gain noise, where the proportionality constant between analog signal out and number of photons varies randomly. Thus, the excess noise factor of a photon-counting detector is unity, and the achievable signal-to-noise ratio for a fixed number of photons is generally higher than the same detector without photon counting.[3]
[Photon counting] / can improve temporal resolution. In a conventional detector, multiple arriving photons generate overlapping impulse responses, limiting temporal resolution to approximately the fall time of the detector. However, if it is known that a single photon was detected, the center of the impulse response can be evaluated to precisely determine its arrival time. Using time-correlated single-photon counting (TCSPC), temporal resolution of less than 25 ps has been demonstrated using detectors with a fall time more than 20 times greater.[4]

[-0] 
[+0] Prepare required environment setup and define the medium object.
[+1] Pass the completion parameters for openai as dictionary of standard form.
[*1] Calculate the screened environment image and resource picture.

**Environments and Agents**
- list of all environment substrates and associated agents
- dictionary containing set of tasks being possible on the environments under agent composition
- regular network of possible tasks and nodes connecting their endpoints

**Pole**
- mono
- di
- biquad
- linequad

**Sound Fields Radiated by Simple Sources**

[-1] Radiation from a monopole source

- A monopole is a source which radiates sound equally well in all directions.
1 The simplest example of a monopole source would be a sphere whose radius alternately expands and contracts sinusoidally.
- The monopole source creates a sound wave by alternately introducing and removing fluid into the surrounding area.
- A boxed loudspeaker at low frequencies acts as a monopole. - The directivity pattern for a monopole source to be shown along with the code.
- Show the pressure field produced by a monopole source.
- Individual points on the grid would simply move back and forth about some equilibrium position while the spherical wave expands outwards.

[-0] Radiation from a dipole source

- Create an animation showing particle motion in radiated sound field from a dipole source
- Create the directivity plot for a dipole

- A dipole source consists of two monopole sources of equal strength but opposite phase and separated by a small distance compared with the wavelength of sound.
- While one source expands the other source contracts.
- The result is that the fluid (air) near the two sources sloshes back and forth to produce the sound.
- A sphere which oscillates back and forth acts like a dipole source, as does an unboxed loudspeaker (while the front is pushing outwards the back is sucking in).

- A dipole source does not radiate sound in all directions equally.
- The directivity pattern would have to be shown with code that looks like a figure-8
- There are two regions where sound is radiated very well, and two regions where sound cancels.

- The visualization should show the pressure field produced by a dipole source.
- At the center of the pressure field there would exist the sloshing back and forth caused by the dipole motion.
- The regions where sound is cancelled should show up along the vertical axes (the grid motion would be almost zero).
- Furthermore, the wavefronts expanding to the right and left would have to be 180 degree out of phase with each other.

[+0] Radiation from a lateral quadrupole source

- If two opposite phase monopoles make up a dipole, then two opposite dipoles make up a quadrupole source.
- In a Lateral Quadrupole arrangement the two dipoles do not lie along the same line (four monopoles with alternating phase at the corners of a square).
- The directivity pattern for a lateral quadrupole looks like a clover-leaf pattern; sound is radiated well in front of each monopole source, but sound is canceled at points equidistant from adjacent opposite monopoles.

- Show the pressure field produced by a lateral quadrupole source.
- At the center of the pressure field you can see the quadrupole motion as the particles alternate motion in the horizontal and vertical directions. back and forth caused by the dipole motion.
- The regions where sound is cancelled shows up along the diagonals (where the grid motion is almost zero). 
- Furthermore, there is a 180 degree phase difference between the horizontal and vertical wavefronts.

[+1] Radiation from a linear quadrupole source

- Animation showing the particle motion in the radiated sound field from a linear quadrupole source
- Plot directivity plot for the near-field of a linear quadrupole
- If two opposite phase dipoles lie along the same line they make up a Linear Quadrupole source.
- A tuning fork is a good example of a linear quadrupole source (each tine acts as a dipole as it vibrates back and forth, and the two tines oscillate in opposite directions). - What makes the linear quadrupole interesting is that there is a very obvious transition from near field to far field.
- In the near field there are four maxima and four minima, with the maxima along the quadrupole axis about 5dB louder than the maxima perpendicular to the quadrupole axis.

- The near field directivity pattern is shown at right.

- In the far field there are only two maxima (along the quadrupole axis) and two minima (perpendicular to the quadrupole axis) as shown in the figure below right.

- The directivity plot for the far-field of a linear quadrupole The animated GIF movie at left shows the pressure field radiated by a linear quadrupole. At the center of the picture you can see the quadrupole near field pattern. As the wave expands outwards it becomes almost a spherical wave (notice that the left and right going wavefronts are in phase as opposed to the dipole source) except that the amplitude is severely reduced in the vertical directions.
