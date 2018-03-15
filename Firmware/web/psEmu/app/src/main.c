#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

typedef enum {
	mode_off,                   //!< mode_off
	mode_overcurrentShutdown,	//!< mode_overcurrentShutdown
	mode_limitation,         	//!< mode_limitation
	mode_timeShutdown,       	//!< mode_timeShutdown
	mode_lowCurrentShutdown, 	//!< mode_lowCurrentShutdown
	mode_Uadj,                  //!< mode_Uadj
	mode_Iadj,                  //!< mode_Iadj

	mode_raw,
} psMode_type;

typedef enum {
	setNone,
	setSwitchOn,
	setSwitchOff,
	setSavePointU0,
	setSavePointU1,
	setSavePointU2,
	setSavePointU3,
	setSavePointI0,
	setSavePointI1,
	setSavePointI2,
	setSavePointI3,
	setSaveSettings
} request_type;

typedef union {
	struct {
		uint32_t ovfCurrent :1;
		uint32_t switchIsON :1;
		uint32_t modeIlim :1;

		//Аварии
		uint32_t ovfLinearRegTemper :1;
		uint32_t errorLinearRegTemperSens :1;
		uint32_t lowInputVoltage :1;
		uint32_t reverseVoltage :1;
		uint32_t noCalibration :1;
	} bit;
	uint32_t all;
} psState_type;

typedef struct {
	uint32_t power;          ///< [X_XXX Wt]
	uint32_t resistens;      ///< [X_XXX Ohm]
	uint32_t time;           ///< [s]
	uint32_t capacity;       ///< [X_XXX Ah]
	uint32_t u;              ///< [X_XXXXXX V]
	uint32_t i;              ///< [X_XXXXXX A]
	uint16_t adcu;           ///< [LSB]
	uint16_t adci;           ///< [LSB]
	uint16_t uin;            ///< [mV]
	uint16_t temperatureLin; ///< [X_X °С]
} meas_type;

typedef struct {
	uint32_t u;              ///< [X_XXXXXX V]
	uint32_t i;              ///< [X_XXXXXX A]
	uint32_t time;           ///< [s]
	uint16_t dacu;           ///< [LSB]
	uint16_t daci;           ///< [LSB]
	request_type request 	:8;
	psMode_type mode 		:8;
} task_type;

typedef struct {
	psState_type state;
	meas_type meas;
	task_type task;
} transfer_type;

transfer_type m = {
	.meas = {
		.power			= 1,           		///< [X_XXX Wt]
		.resistens		= 2,      			///< [X_XXX Ohm]
		.time			= 3,           		///< [s]
		.capacity		= 25456,       		///< [X_XXX A/h]
		.u				= 22220000,       	///< [X_XXXXXX V]
		.i				= 0,      			///< [X_XXXXXX A]
		.adcu			= 15,           	///< [LSB]
		.adci			= 16,          		///< [LSB]
		.uin			= 17,           	///< [X_XXX V]
		.temperatureLin	= 18, 				///< [X_X °С]
	},
	.task = {
		.u				= 25123000,			///< [X_XXXXXX V]
		.i				= 456000,      		///< [X_XXXXXX A]
	},
};

#define KNRM  "\x1B[0m"
#define KRED  "\x1B[31m"

int main(int argc, char *argv[]){
	setvbuf(stdout, NULL, _IONBF, 0);	//not buffered

	uint32_t counter = 0;

	while(1){
		m.state.bit.ovfCurrent ^= 1;
		m.state.bit.modeIlim ^= 1;
		m.state.bit.switchIsON ^= 1;
		m.meas.time++;
		m.meas.i += 100000;
		if(m.meas.i > 10000000){
			m.meas.i -= 10000000;
		}

		printf(KRED);
		printf("%u \t", counter++);
		printf(KNRM);

		int fd = open("D:/Radio/Devices/PS3604L/Firmware/web/html/statemeastask.bin", O_CREAT | O_RDWR, S_IWUSR);
		if(fd != -1){
			printf("file is created, ");
		}
		size_t sizebin = sizeof(m);
		write(fd, &m, sizeof(m));
		printf("write %lu bytes\r", sizebin);

		close(fd);

		usleep(2000 * 1000);
	}
}
