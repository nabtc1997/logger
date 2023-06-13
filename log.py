        except Exception as error:
            logger.info(f'{address} | {type_} : {error}')
            await asyncio.sleep(3)
