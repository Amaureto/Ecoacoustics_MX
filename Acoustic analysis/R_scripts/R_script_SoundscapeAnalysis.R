install.packages("soundecology")
install.packages("tuneR")
install.packages("seewave")
install.packages("pumilioR")

####Recordatorios: Fijar carpeta de trabajo y activar paquetes

#Cargamos paquete "soundecology" y sus dependencias
library("soundecology")
library("seewave")
library("tuneR")
library("pumilioR")

?spectro

SonidoA1<-readWave("agriculturaDeTemporal_Ver_9am.wav")

  Sonido<-readWave("agriculturaDeTemporal_Ver_9am.wav",from=0, to=60, units="seconds")
  Sonido
  
SonidoE5<-readWave("ciudad_DF_830am_5.wav")
OscillogramE5<-oscillo(SonidoE5)
SpectrogramE5<-spectro(SonidoE5,f=22050,type="l")
MeanspecE5<-meanspec(SonidoE5,f=22050,wl=512,type="l",col="blue")

SonidoI2<-readWave("SelvaSubhumedaCaducifolia_SierraHuautlaMorelos_730am_2.wav")
OscillogramI2<-oscillo(SonidoI2)
SpectrogramI2<-spectro(SonidoI2,f=22050,type="l")
MeanspecI2<-meanspec(SonidoI2,f=22050,wl=512,type="l",col="blue")

SonidoG1<-readWave("selvaAltaPerennifolia_estacionLosTuxtlas_Ver_830am_1.wav")
OscillogramG1<-oscillo(SonidoG1)
SpectrogramG1<-spectro(SonidoG1,f=22050,type="l")
MeanspecG1<-meanspec(SonidoG1,f=22050,wl=512,type="l",col="blue")

SonidoH2<-readWave("SelvaSubhumedaCaducifolia_SierraHuautlaMorelos_730am_2.wav")
OscillogramH2<-oscillo(SonidoH2)
SpectrogramH2<-spectro(SonidoH2,f=22050,type="l")
MeanspecH2<-meanspec(SonidoH2,f=22050,wl=512,type="l",col="blue")

SonidoI2<-readWave("SelvaSubhumedaCaducifolia_SierraHuautlaMorelos_9am_2.wav")
OscillogramI2<-oscillo(SonidoI2)
SpectrogramI2<-spectro(SonidoI2,f=22050,type="l")
MeanspecI2<-meanspec(SonidoI2,f=22050,wl=512,type="l",col="blue")

SonidoG5<-readWave("selvaAltaPerennifolia_estacionLosTuxtlas_Ver_830am_5.wav")
OscillogramG5<-oscillo(SonidoG5)
SpectrogramG5<-spectro(SonidoG5,f=22050,type="l")
MeanspecG5<-meanspec(SonidoG5,f=22050,wl=512,type="l",col="blue")

SonidoA4<-readWave("agriculturaDeTemporal_Ver_9am_4.wav")
OscillogramA4<-oscillo(SonidoG5)
SpectrogramA4<-spectro(SonidoA4,f=22050,type="l")
MeanspecA4<-meanspec(SonidoA4,f=22050,wl=512,type="l",col="blue")


OscillogramA1<-oscillo(SonidoA1)
SpectrogramA1<-spectro(SonidoA1,f=22050,type="l")
MeanspecA1<-meanspec(SonidoA1,f=22050,wl=512,type="l",col="blue")

dev.off()

op<-par(bg="white", mfrow=c(3,1))


